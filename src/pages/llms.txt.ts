// Plain-text fact sheet for AI assistants (https://llmstxt.org). Generated from the same
// data as the site, so its numbers and paper list can never drift from the pages.
import type { APIRoute } from 'astro';
import { site, emailText } from '../config/site';
import { experience, libraries, talks } from '../lib/data';
import { getPubs, getStats, getAreas, isMine, isPeerReviewed, authorsOf, pageOf, fill, plainOf, ROLE_LABEL, type Pub } from '../lib/pubs';
import { getStars } from '../lib/remote';

export const GET: APIRoute = async () => {
  const s = await getStats();
  const pubs = (await getPubs()).filter(isMine);
  const areas = await getAreas();
  const libs = await Promise.all(libraries.map(async (l) => ({ ...l, n: await getStars(l.repo, l.stars) })));
  const u = (p: string) => new URL(p, site.url).href;
  const plain = (t: string) => t.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1').replace(/\*+/g, '');
  const gist = (p: Pub) => (plainOf(p) ? ` In plain words: ${plainOf(p)}` : '');
  const role = (p: Pub) => (p.data.myRole ? ` His role: ${ROLE_LABEL[p.data.myRole].toLowerCase()}.` : '');
  const current = experience[0].roles[0];
  const currentPoints = await Promise.all(current.points.map(async (pt) => `- ${pt.label ? pt.label + ': ' : ''}${plain(await fill(pt.text))}`));

  const lines = [
    `# ${site.name}`,
    '',
    `> ${site.role} at ${site.org}, leading the Model Science group. Works on post-training safety, alignment and mechanistic interpretability for language models; earlier work on tabular foundation models, climate AI, medical imaging and NLP. ${s.papersLabel} papers (${s.peerReviewed} peer-reviewed), ${s.citationsRounded} Google Scholar citations, h-index ${s.hIndex}. B.Tech Data Science & Engineering, Manipal Institute of Technology (2024). AAAI Undergraduate Consortium Scholar (2023) and Mentor (2026).`,
    '',
    `Research question: ${site.thesis}`,
    '',
    '## Current role (in his own words)',
    '',
    `${plain(current.role)}, ${current.date}.`,
    '',
    ...currentPoints,
    '',
    'Role labels below: "led" means first, co-first or main hands-on author; "senior author" means he mentored the first author or led the design.',
    '',
    ...(talks.notice ? ['## Notice', '', talks.notice, ''] : []),
    '## Pages',
    '',
    `- [Home](${u('/')}): bio, research threads, selected work, citations, news, contact.`,
    `- [Publications](${u('/publications/')}): all ${s.papersLabel} papers by area, each with its own page (abstract, BibTeX, links).`,
    `- [Experience](${u('/experience/')}): Lexsi Labs, Mila Quebec AI Institute, Bosch Research, IIT Kharagpur, and earlier roles.`,
    `- [Talks & Events](${u('/talks-events/')}): talks, posters and conferences.`,
    `- [Writing](${u('/writing/')}): notes on the research.`,
    `- [Education & Service](${u('/education-service/')}): education, honors, reviewing, skills, collaborators.`,
    '',
    '## Contact',
    '',
    `- Email (written to avoid spam harvesting; replace [at] with @ and [dot] with .): ${emailText}`,
    `- Open to: ${site.openTo.join(', ')}`,
    ...Object.entries(site.links).map(([k, v]) => `- ${k}: ${v}`),
    '',
    '## Peer-reviewed papers',
    '',
    ...areas.flatMap((area) => {
      const list = pubs.filter((p) => p.data.area === area && isPeerReviewed(p));
      return list.length
        ? [`### ${area}`, ...list.map((p) => `- [${p.data.title}](${u(pageOf(p))}): ${authorsOf(p).map((a) => a.name).join(', ')}. ${p.data.venue}, ${p.data.year}.${role(p)}${gist(p)}`), '']
        : [];
    }),
    '## Pre-prints and work under review',
    '',
    ...pubs.filter((p) => !isPeerReviewed(p)).map((p) => `- [${p.data.title}](${u(pageOf(p))}): ${p.data.venue}, ${p.data.year}.${role(p)}${gist(p)}`),
    '',
    '## Libraries & tools',
    '',
    ...libs.map((l) => `- ${l.name} (${l.n} GitHub stars, ${l.role.toLowerCase()}): ${l.description} https://github.com/${l.repo}`),
    '',
  ];
  return new Response(lines.join('\n'), { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
