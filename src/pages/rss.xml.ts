import rss from '@astrojs/rss';
import type { APIRoute } from 'astro';
import { site } from '../config/site';
import { getPosts } from '../lib/posts';

export const GET: APIRoute = async () => {
  const posts = (await getPosts()).filter((p) => !p.data.draft);
  return rss({
    title: `${site.name}: Writing`,
    description: 'Notes on post-training safety, mechanistic interpretability and the research behind the papers.',
    site: site.url,
    items: posts.map((p) => ({
      title: p.data.title,
      description: p.data.description,
      pubDate: p.data.date,
      link: `/writing/${p.id}/`,
    })),
  });
};
