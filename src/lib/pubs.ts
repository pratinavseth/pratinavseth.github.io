// Everything derived from publications.yaml: counts, collaborator lists, BibTeX, labels.
// Pages never hand-type a number; they read it from here.
import { getCollection, type CollectionEntry } from 'astro:content';
import { collaborators as collabMeta, libraries } from './data';
import { getScholar, getStars } from './remote';
import { site } from '../config/site';
import abstractsJson from '../data/abstracts.json';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';

export type Pub = CollectionEntry<'publications'>;
const abstracts = abstractsJson as Record<string, { abstract: string; published?: string }>;

export const ME = 'Pratinav Seth';

export interface Author {
  name: string;
  me: boolean;
  equal: boolean;
}

export function authorsOf(p: Pub): Author[] {
  return p.data.authors.map((raw) => {
    const equal = raw.endsWith('*');
    const name = equal ? raw.slice(0, -1).trim() : raw;
    return { name, me: name === ME, equal };
  });
}

export const isMine = (p: Pub) => authorsOf(p).some((a) => a.me);
export const isPeerReviewed = (p: Pub) => p.data.status === 'published';

export const STATUS_LABEL: Record<Pub['data']['status'], string> = {
  published: 'Peer-reviewed',
  preprint: 'Pre-print',
  'under-review': 'Under review',
  report: 'Technical report',
};

export const TYPE_LABEL: Record<Pub['data']['type'], string> = {
  conference: 'Conference',
  journal: 'Journal',
  workshop: 'Workshop',
  demo: 'Demo',
  'shared-task': 'Shared task',
  'tiny-paper': 'Tiny paper',
  'student-abstract': 'Student abstract',
  preprint: 'Pre-print',
  'under-review': 'Under review',
  report: 'Report',
};

export const ROLE_LABEL: Record<'lead' | 'senior' | 'coauthor', string> = {
  lead: 'Lead author',
  senior: 'Senior author',
  coauthor: 'Co-author',
};
export const ROLE_HINT: Record<'lead' | 'senior' | 'coauthor', string> = {
  lead: 'First author or main hands-on contributor',
  senior: 'Mentored the first author or led the design',
  coauthor: 'Co-author',
};

export const abstractOf = (p: Pub) => (p.data.arxiv ? abstracts[p.data.arxiv]?.abstract : undefined);

export function pdfOf(p: Pub): string | undefined {
  if (p.data.arxiv) return `https://arxiv.org/pdf/${p.data.arxiv}`;
  const u = p.data.url;
  if (u && /\.pdf($|\?)|\/pdf\/|openreview\.net\/pdf|download/.test(u)) return u;
  return undefined;
}

export const pageOf = (p: Pub) => `/publications/${p.id}/`;

// getCollection() returns entries sorted by id; the data file's own order is curated
// (newest and most important first within each area), so restore it.
const fileOrder = new Map(
  [...readFileSync(join(process.cwd(), 'src/data/publications.yaml'), 'utf8').matchAll(/^- id: "?([^"\s]+)"?\s*$/gm)].map(
    (m, i) => [m[1], i] as const,
  ),
);

let cache: Promise<Pub[]> | undefined;
/** All papers in data-file order. */
export function getPubs(): Promise<Pub[]> {
  cache ??= getCollection('publications').then((all) =>
    all.sort((a, b) => (fileOrder.get(a.id) ?? 1e9) - (fileOrder.get(b.id) ?? 1e9)),
  );
  return cache;
}

export async function citationsOf(p: Pub): Promise<number | undefined> {
  if (!p.data.scholarId) return undefined;
  const s = await getScholar();
  return s.publications[`${site.scholarUser}:${p.data.scholarId}`]?.num_citations;
}

/** Areas in the order they first appear in the data file. */
export async function getAreas(): Promise<string[]> {
  const pubs = await getPubs();
  return [...new Set(pubs.map((p) => p.data.area))];
}

export interface Stats {
  papers: number;
  peerReviewed: number;
  citations: number;
  citationsRounded: string;
  hIndex: number;
  citesPerYear: [string, number][];
  ossLibraries: number;
  stars: number;
  starsRounded: string;
  scholarUpdated?: string;
}

const roundDown = (n: number, step: number) => `${Math.floor(n / step) * step}+`;

let statsCache: Promise<Stats> | undefined;
export function getStats(): Promise<Stats> {
  statsCache ??= (async () => {
    const pubs = (await getPubs()).filter(isMine);
    const scholar = await getScholar();
    const oss = libraries.filter((l) => l.oss);
    const stars = (await Promise.all(oss.map((l) => getStars(l.repo, l.stars)))).reduce((a, b) => a + b, 0);
    return {
      papers: pubs.length,
      peerReviewed: pubs.filter(isPeerReviewed).length,
      citations: scholar.citedby,
      citationsRounded: roundDown(scholar.citedby, 10),
      hIndex: scholar.hindex,
      citesPerYear: Object.entries(scholar.cites_per_year).sort(([a], [b]) => a.localeCompare(b)),
      ossLibraries: oss.length,
      stars,
      starsRounded: roundDown(stars, 50),
      scholarUpdated: scholar.updated?.slice(0, 10),
    };
  })();
  return statsCache;
}

/** Replace {papers}, {peerReviewed}, {citations}, {stars}, {hIndex}, {ossLibraries} in prose. */
export async function fill(text: string): Promise<string> {
  const s = await getStats();
  const words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'];
  const word = (n: number) => words[n] ?? String(n);
  const cap = (t: string) => t.charAt(0).toUpperCase() + t.slice(1);
  const map: Record<string, string> = {
    papers: String(s.papers),
    // {ossLibrariesWord} → "seven", {OssLibrariesWord} → "Seven" (for the start of a sentence)
    ossLibrariesWord: word(s.ossLibraries),
    OssLibrariesWord: cap(word(s.ossLibraries)),
    peerReviewed: String(s.peerReviewed),
    citations: s.citationsRounded,
    stars: s.starsRounded,
    hIndex: String(s.hIndex),
    ossLibraries: String(s.ossLibraries),
  };
  return text.replace(/\{(\w+)\}/g, (m, k: string) => map[k] ?? m);
}

export interface Collaborator {
  name: string;
  count: number;
  institution?: string;
  role: 'manager' | 'mentor' | 'mentee' | 'collaborator';
  papers: { title: string; href: string }[];
}

export async function getCollaborators(): Promise<Collaborator[]> {
  const pubs = (await getPubs()).filter(isMine);
  const byName = new Map<string, Collaborator>();
  for (const p of pubs) {
    for (const a of authorsOf(p)) {
      if (a.me) continue;
      const meta = collabMeta[a.name];
      if (!meta) console.warn(`[collaborators] No entry for "${a.name}" in src/data/collaborators.yaml`);
      const c = byName.get(a.name) ?? {
        name: a.name,
        count: 0,
        institution: meta?.institution,
        role: meta?.role ?? 'collaborator',
        papers: [],
      };
      c.count++;
      c.papers.push({ title: p.data.title, href: pageOf(p) });
      byName.set(a.name, c);
    }
  }
  return [...byName.values()].sort((a, b) => b.count - a.count || a.name.localeCompare(b.name));
}

function bibKey(p: Pub): string {
  const first = authorsOf(p)[0]?.name.split(' ').pop()?.toLowerCase().replace(/[^a-z]/g, '') || 'anon';
  const word = p.data.title.toLowerCase().replace(/[^a-z0-9 ]/g, '').split(' ').find((w) => w.length > 3) ?? 'paper';
  return `${first}${p.data.year}${word}`;
}

export function bibtex(p: Pub): string {
  const authors = authorsOf(p).map((a) => a.name).join(' and ');
  const kind = p.data.type === 'journal' ? 'article' : p.data.status === 'published' ? 'inproceedings' : 'misc';
  const fields: [string, string | undefined][] = [
    ['title', `{${p.data.title}}`],
    ['author', authors],
    [kind === 'article' ? 'journal' : kind === 'inproceedings' ? 'booktitle' : 'note', p.data.venue],
    ['year', String(p.data.year)],
    ['eprint', p.data.arxiv],
    ['archivePrefix', p.data.arxiv ? 'arXiv' : undefined],
    ['url', p.data.url ?? (p.data.arxiv ? `https://arxiv.org/abs/${p.data.arxiv}` : undefined)],
  ];
  const body = fields
    .filter(([, v]) => v)
    .map(([k, v]) => `  ${k.padEnd(13)} = {${v}}`)
    .join(',\n');
  return `@${kind}{${bibKey(p)},\n${body}\n}`;
}
