// Fetches abstracts for every paper in src/data/publications.yaml that has an `arxiv` id,
// and writes them to src/data/abstracts.json. Existing entries are kept, so hand edits survive.
//
//   npm run fetch:abstracts            # only papers missing an abstract
//   npm run fetch:abstracts -- --all   # refetch everything
//
// Tries the arXiv API first (one request for all papers); if that is rate-limited, falls back to
// reading each paper's arxiv.org/abs page politely, a few seconds apart.
import { readFile, writeFile } from 'node:fs/promises';

const PUBS = new URL('../src/data/publications.yaml', import.meta.url);
const OUT = new URL('../src/data/abstracts.json', import.meta.url);
const refetchAll = process.argv.includes('--all');
const sleep = (s) => new Promise((r) => setTimeout(r, s * 1000));

const yaml = await readFile(PUBS, 'utf8');
const ids = [...yaml.matchAll(/^\s+arxiv:\s*"?([0-9]{4}\.[0-9]{4,5})"?\s*$/gm)].map((m) => m[1]);

let existing = {};
try {
  existing = JSON.parse(await readFile(OUT, 'utf8'));
} catch {}

const wanted = ids.filter((id) => refetchAll || !existing[id]);
if (wanted.length === 0) {
  console.log('All abstracts present.');
  process.exit(0);
}

const decode = (s) =>
  s
    .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#0?39;/g, "'")
    .replace(/&#x27;/g, "'").replace(/&amp;/g, '&');
// Light LaTeX cleanup (Greek letters, \emph, \%, \times, inline $…$, stray %). Edit abstracts.json for anything else.
const GREEK = { alpha: 'α', beta: 'β', gamma: 'γ', delta: 'δ', Delta: 'Δ', theta: 'θ', Theta: 'Θ', lambda: 'λ', mu: 'μ', sigma: 'σ', epsilon: 'ε' };
const delatex = (s) =>
  s
    .replace(/\\emph\{([^}]*)\}/g, '$1')
    .replace(/\{?\\(alpha|beta|gamma|delta|Delta|theta|Theta|lambda|mu|sigma|epsilon)\}?/g, (_, g) => GREEK[g])
    .replace(/\\%/g, '%')
    .replace(/\\times/g, '×')
    .replace(/\$([^$]*)\$/g, '$1')
    .replace(/%\s*$/, '');
const clean = (s) => delatex(decode(s)).replace(/\s+/g, ' ').replace(/ \./g, '.').trim();

async function viaApi() {
  const res = await fetch(`https://export.arxiv.org/api/query?id_list=${wanted.join(',')}&max_results=${wanted.length}`);
  if (!res.ok) throw new Error(`arXiv API ${res.status}`);
  const xml = await res.text();
  let n = 0;
  for (const [, entry] of xml.matchAll(/<entry>([\s\S]*?)<\/entry>/g)) {
    const id = entry.match(/<id>https?:\/\/arxiv\.org\/abs\/([0-9.]+)/)?.[1];
    const summary = entry.match(/<summary>([\s\S]*?)<\/summary>/)?.[1];
    if (!id || !summary) continue;
    existing[id] = { abstract: clean(summary), published: entry.match(/<published>([^<]{10})/)?.[1] };
    n++;
  }
  return n;
}

async function viaPages() {
  let n = 0;
  for (const id of wanted) {
    if (existing[id] && !refetchAll) continue;
    for (const wait of [0, 20, 60]) {
      if (wait) await sleep(wait);
      const res = await fetch(`https://arxiv.org/abs/${id}`, { headers: { 'User-Agent': 'pratinavseth.github.io abstract fetcher (mailto:seth.pratinav@gmail.com)' } });
      if (res.status === 429 || res.status === 503) continue;
      if (!res.ok) break;
      const html = await res.text();
      const abs = html.match(/<meta name="citation_abstract" content="([^"]*)"/)?.[1];
      const date = html.match(/<meta name="citation_date" content="([^"]*)"/)?.[1];
      if (abs) {
        existing[id] = { abstract: clean(abs), published: date?.replace(/\//g, '-') };
        n++;
        console.log(`  ${id} ok`);
      }
      break;
    }
    await sleep(3);
  }
  return n;
}

let added;
try {
  added = await viaApi();
} catch (e) {
  console.log(`${e.message}; falling back to individual arXiv pages (slow, ~3s each)`);
  added = await viaPages();
}

const sorted = Object.fromEntries(Object.keys(existing).sort().map((k) => [k, existing[k]]));
await writeFile(OUT, JSON.stringify(sorted, null, 2) + '\n');
console.log(`Fetched ${added} of ${wanted.length} abstracts -> src/data/abstracts.json`);
