// Build-time fetches for numbers that change on their own (citations, GitHub stars).
// Each falls back to a committed snapshot, so an offline build or an API outage
// never breaks the site — it just shows the last known numbers.
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { site } from '../config/site';

export interface ScholarData {
  updated?: string;
  citedby: number;
  hindex: number;
  i10index?: number;
  cites_per_year: Record<string, number>;
  publications: Record<string, { num_citations: number }>;
}

async function fetchJson<T>(url: string, extraHeaders: Record<string, string> = {}, ms = 8000): Promise<T | undefined> {
  if (process.env.OFFLINE) return undefined;
  try {
    const res = await fetch(url, {
      signal: AbortSignal.timeout(ms),
      headers: { 'User-Agent': 'pratinavseth.github.io build', Accept: 'application/json', ...extraHeaders },
    });
    if (!res.ok) return undefined;
    return (await res.json()) as T;
  } catch {
    return undefined;
  }
}

let scholarPromise: Promise<ScholarData & { live: boolean }> | undefined;

/** Google Scholar stats written daily to the google-scholar-stats branch by the crawler workflow. */
export function getScholar() {
  scholarPromise ??= (async () => {
    const snapshot = JSON.parse(
      readFileSync(join(process.cwd(), 'src/data/scholar-snapshot.json'), 'utf8'),
    ) as ScholarData;
    const live = await fetchJson<ScholarData>(site.scholarDataUrl);
    // Citations only go up; never let a partial crawl lower the shown numbers.
    if (live && live.citedby >= snapshot.citedby && live.publications) return { ...live, live: true };
    return { ...snapshot, live: false };
  })();
  return scholarPromise;
}

const starCache = new Map<string, Promise<number>>();

/** GitHub stargazer count for "owner/repo", or the fallback when the API is unavailable/rate-limited. */
export function getStars(repo: string, fallback: number): Promise<number> {
  if (!starCache.has(repo)) {
    // In GitHub Actions the workflow token lifts the 60-requests/hour anonymous limit.
    const auth: Record<string, string> = process.env.GITHUB_TOKEN ? { Authorization: `Bearer ${process.env.GITHUB_TOKEN}` } : {};
    starCache.set(
      repo,
      (async () => {
        const data = await fetchJson<{ stargazers_count?: number }>(`https://api.github.com/repos/${repo}`, auth);
        const n = data?.stargazers_count;
        return typeof n === 'number' && n >= fallback ? n : fallback;
      })(),
    );
  }
  return starCache.get(repo)!;
}
