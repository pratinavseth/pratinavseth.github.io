import type { APIRoute, GetStaticPaths } from 'astro';
import { paperOg } from '../../../lib/og';
import { authorsOf, getPubs, type Pub } from '../../../lib/pubs';

export const getStaticPaths = (async () => {
  const pubs = await getPubs();
  return pubs.map((pub) => ({ params: { id: pub.id }, props: { pub } }));
}) satisfies GetStaticPaths;

export const GET: APIRoute<{ pub: Pub }> = async ({ props }) => {
  const d = props.pub.data;
  const names = authorsOf(props.pub).map((a) => a.name);
  const png = await paperOg({
    title: d.title,
    venue: d.venue,
    year: d.year,
    authors: names.length > 6 ? `${names.slice(0, 5).join(', ')} and ${names.length - 5} others` : names.join(', '),
  });
  return new Response(new Uint8Array(png), { headers: { 'Content-Type': 'image/png' } });
};
