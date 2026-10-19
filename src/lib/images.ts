import type { ImageMetadata } from 'astro';

// Every image under src/assets/images, keyed by its path relative to that folder
// (e.g. "circuitkit-fig.png", "events/icml2025-alberta-wells.jpg").
const files = import.meta.glob<{ default: ImageMetadata }>('/src/assets/images/**/*.{png,jpg,jpeg,webp}', { eager: true });

const byName = new Map(
  Object.entries(files).map(([path, mod]) => [path.replace('/src/assets/images/', ''), mod.default]),
);

export function img(name: string): ImageMetadata {
  const found = byName.get(name);
  if (!found) throw new Error(`Image "${name}" not found in src/assets/images/`);
  return found;
}

export const hasImg = (name?: string) => !!name && byName.has(name);
