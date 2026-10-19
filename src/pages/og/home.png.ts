import type { APIRoute } from 'astro';
import { homeOg } from '../../lib/og';
import { getStats } from '../../lib/pubs';
import { site } from '../../config/site';

export const GET: APIRoute = async () => {
  const s = await getStats();
  const png = await homeOg({
    thesis: `${site.role}, ${site.org}. ${site.tagline}`,
    stats: `${s.peerReviewed} PEER-REVIEWED · ${s.citationsRounded} CITATIONS · ${s.ossLibraries} OSS LIBRARIES`,
  });
  return new Response(new Uint8Array(png), { headers: { 'Content-Type': 'image/png' } });
};
