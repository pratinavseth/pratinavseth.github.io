// Plain-text fact sheet for AI assistants (https://llmstxt.org). Generated from the same
// data as the site, so its numbers and paper list can never drift from the pages.
import type { APIRoute } from 'astro';
import { site } from '../config/site';
import { libraries } from '../lib/data';
import { getPubs, getStats, getAreas, isMine, isPeerReviewed, authorsOf, pageOf } from '../lib/pubs';
import { getStars } from '../lib/remote';

export const GET: APIRoute = async () => {
  const s = await getStats();
  const pubs = (await getPubs()).filter(isMine);
  const areas = await getAreas();
  const libs = await Promise.all(libraries.map(async (l) => ({ ...l, n: await getStars(l.repo, l.stars) })));
  const u = (p: string) => new URL(p, site.url).href;

  const lines = [
    `# ${site.name}`,
    '',
    `> ${site.role} at ${site.org}, leading the Model Science group (India & Paris). Works on post-training safety, alignment and mechanistic interpretability for language models; earlier work on tabular foundation models, climate AI, medical imaging and NLP. ${s.papers} papers (${s.peerReviewed} peer-reviewed), ${s.citations} Google Scholar citations, h-index ${s.hIndex}. B.Tech Data Science & Engineering, Manipal Institute of Technology (2024). AAAI Undergraduate Consortium Scholar (2023) and Mentor (2026).`,
    '',
    `Research question: ${site.thesis}`,
    '',
    '## Pages',
    '',
    `- [Home](${u('/')}): bio, research threads, selected work, citations, news, contact.`,
    `- [Publications](${u('/publications/')}): all ${s.papers} papers by area, each with its own page (abstract, BibTeX, links).`,
    `- [Experience](${u('/experience/')}): Lexsi Labs, Mila Quebec AI Institute, Bosch Research, IIT Kharagpur, and earlier roles.`,
    `- [Talks & Events](${u('/talks-events/')}): talks, posters and conferences.`,
    `- [Writing](${u('/writing/')}): notes on the research.`,
    `- [Education & Service](${u('/education-service/')}): education, honors, reviewing, skills, collaborators.`,
    '',
    '## Contact',
    '',
    `- Email: ${site.email}`,
    `- Open to: ${site.openTo.join(', ')}`,
    ...Object.entries(site.links).map(([k, v]) => `- ${k}: ${v}`),
    '',
    '## Peer-reviewed papers',
    '',
    ...areas.flatMap((area) => {
      const list = pubs.filter((p) => p.data.area === area && isPeerReviewed(p));
      return list.length
        ? [`### ${area}`, ...list.map((p) => `- [${p.data.title}](${u(pageOf(p))}): ${authorsOf(p).map((a) => a.name).join(', ')}. ${p.data.venue}, ${p.data.year}.`), '']
        : [];
    }),
    '## Pre-prints and work under review',
    '',
    ...pubs.filter((p) => !isPeerReviewed(p)).map((p) => `- [${p.data.title}](${u(pageOf(p))}): ${p.data.venue}, ${p.data.year}.`),
    '',
    '## Libraries & tools',
    '',
    ...libs.map((l) => `- ${l.name} (${l.n} GitHub stars, ${l.role.toLowerCase()}): ${l.description} https://github.com/${l.repo}`),
    '',
  ];
  return new Response(lines.join('\n'), { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
