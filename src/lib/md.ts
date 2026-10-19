import { marked } from 'marked';

marked.use({ gfm: true });

const EXTERNAL = /^https?:\/\//;

/** Render a one-line Markdown string (links, bold, italics, code) to HTML. External links open safely. */
export function inline(text: string): string {
  const html = marked.parseInline(text, { async: false }) as string;
  return html.replace(/<a href="([^"]+)"/g, (m, href: string) =>
    EXTERNAL.test(href) && !href.startsWith('https://pratinavseth.github.io')
      ? `<a href="${href}" rel="noopener"`
      : m,
  );
}

/** Render multi-paragraph Markdown to HTML. */
export function block(text: string): string {
  return marked.parse(text, { async: false }) as string;
}

/** Strip Markdown to plain text (for meta descriptions, llms.txt, JSON-LD). */
export function plain(text: string): string {
  return text
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
    .replace(/[*_`]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}
