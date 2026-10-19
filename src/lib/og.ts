// 1200×630 share images (LinkedIn, X, Slack, WhatsApp previews), rendered at build time with sharp.
// SVG text uses widely installed fonts so it renders the same on Windows and the Linux CI runner.
import sharp from 'sharp';
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { site } from '../config/site';

const W = 1200;
const H = 630;
const PAPER = '#f4f4f0';
const INK = '#0a0a0a';
const RED = '#e61919';
const DISPLAY = "'Archivo Black','Arial Black','DejaVu Sans',Arial,sans-serif";
const SANS = "'IBM Plex Sans','Segoe UI','DejaVu Sans',Arial,sans-serif";
const MONO = "'JetBrains Mono','Consolas','DejaVu Sans Mono',monospace";

const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

/** Greedy word wrap by an approximate character budget per line. */
function wrap(text: string, perLine: number, maxLines: number): string[] {
  const words = text.split(/\s+/);
  const lines: string[] = [];
  let cur = '';
  for (const w of words) {
    if ((cur + ' ' + w).trim().length > perLine && cur) {
      lines.push(cur);
      cur = w;
    } else cur = (cur + ' ' + w).trim();
  }
  if (cur) lines.push(cur);
  if (lines.length > maxLines) {
    const kept = lines.slice(0, maxLines);
    kept[maxLines - 1] = kept[maxLines - 1].replace(/\s*\S*$/, '') + '…';
    return kept;
  }
  return lines;
}

const frame = (inner: string, rightPad = 0) => `
<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
  <rect width="${W}" height="${H}" fill="${PAPER}"/>
  <rect x="0" y="0" width="${W}" height="14" fill="${INK}"/>
  <rect x="64" y="${H - 120}" width="${W - 128 - rightPad}" height="2" fill="${INK}"/>
  <text x="64" y="${H - 66}" font-family="${DISPLAY}" font-size="30" fill="${INK}">${esc(site.name)}</text>
  <text x="${W - 64 - rightPad}" y="${H - 68}" text-anchor="end" font-family="${MONO}" font-size="22" fill="${INK}">pratinavseth.github.io</text>
  ${inner}
</svg>`;

export async function paperOg(opts: { title: string; venue: string; year: number; authors: string }): Promise<Buffer> {
  const titleLines = wrap(opts.title, 36, 4);
  const size = titleLines.length > 3 ? 50 : 58;
  const titleSvg = titleLines
    .map((l, i) => `<text x="64" y="${190 + i * (size + 12)}" font-family="${DISPLAY}" font-size="${size}" fill="${INK}">${esc(l)}</text>`)
    .join('');
  const authorLines = wrap(opts.authors, 78, 2);
  const authorsY = 190 + titleLines.length * (size + 12) + 20;
  const inner = `
    <rect x="64" y="64" width="${Math.min(opts.venue.length * 14 + 40, W - 128)}" height="48" fill="${INK}"/>
    <text x="84" y="96" font-family="${MONO}" font-size="22" fill="${PAPER}">${esc(opts.venue.toUpperCase())} · ${opts.year}</text>
    ${titleSvg}
    ${authorLines.map((l, i) => `<text x="64" y="${authorsY + i * 34}" font-family="${SANS}" font-size="26" fill="#3d3d3d">${esc(l)}</text>`).join('')}
    <rect x="${W - 64 - 90}" y="64" width="90" height="12" fill="${RED}"/>`;
  return sharp(Buffer.from(frame(inner))).png().toBuffer();
}

export async function homeOg(opts: { thesis: string; stats: string }): Promise<Buffer> {
  const photoSize = 400;
  const photo = await sharp(await readFile(join(process.cwd(), 'public', site.avatar)))
    .resize(photoSize, photoSize, { fit: 'cover', position: 'top' })
    .toBuffer();
  const thesis = wrap(opts.thesis, 38, 4);
  const inner = `
    <text x="64" y="150" font-family="${DISPLAY}" font-size="92" fill="${INK}">PRATINAV</text>
    <text x="64" y="245" font-family="${DISPLAY}" font-size="92" fill="${INK}">SETH</text>
    <rect x="64" y="272" width="120" height="10" fill="${RED}"/>
    ${thesis.map((l, i) => `<text x="64" y="${330 + i * 38}" font-family="${SANS}" font-size="29" fill="${INK}">${esc(l)}</text>`).join('')}
    <text x="64" y="${H - 140}" font-family="${MONO}" font-size="22" fill="#3d3d3d">${esc(opts.stats)}</text>
    <rect x="${W - 64 - photoSize - 4}" y="62" width="${photoSize + 8}" height="${photoSize + 8}" fill="${INK}"/>`;
  return sharp(Buffer.from(frame(inner, photoSize + 24)))
    .composite([{ input: photo, left: W - 64 - photoSize, top: 66 }])
    .png()
    .toBuffer();
}
