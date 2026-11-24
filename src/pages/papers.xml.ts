import rss from '@astrojs/rss';
import type { APIRoute } from 'astro';
import { site } from '../config/site';
import { getPubs, isMine, pageOf, plainOf } from '../lib/pubs';
import abstractsJson from '../data/abstracts.json';

const published = abstractsJson as Record<string, { published?: string }>;

/** Paper notes feed: each paper in plain words, dated by its arXiv submission. */
export const GET: APIRoute = async () => {
  const items = (await getPubs())
    .filter((p) => isMine(p) && plainOf(p) && p.data.arxiv && published[p.data.arxiv]?.published)
    .map((p) => ({
      title: p.data.title,
      description: `${plainOf(p)} (${p.data.venue}, ${p.data.year})`,
      pubDate: new Date(published[p.data.arxiv!].published!),
      link: pageOf(p),
    }))
    .sort((a, b) => b.pubDate.getTime() - a.pubDate.getTime());
  return rss({
    title: `${site.name}: Paper notes`,
    description: 'Each paper in plain words, newest first.',
    site: site.url,
    items,
  });
};
