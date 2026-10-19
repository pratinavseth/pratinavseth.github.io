import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { file, glob } from 'astro/loaders';

const STATUS = ['published', 'preprint', 'under-review', 'report'] as const;
const TYPE = [
  'conference', 'journal', 'workshop', 'demo', 'shared-task', 'tiny-paper', 'student-abstract',
  'preprint', 'under-review', 'report',
] as const;

// Every paper on the site. Validated at build time: a typo in status/type, a missing
// title or a duplicate id fails the build instead of shipping a broken page.
const publications = defineCollection({
  loader: file('src/data/publications.yaml'),
  schema: z.object({
    title: z.string().min(1),
    authors: z.array(z.string().min(1)).min(1),
    venue: z.string().min(1),
    status: z.enum(STATUS),
    type: z.enum(TYPE),
    year: z.number().int().min(2015).max(2100),
    area: z.string().min(1),
    myRole: z.enum(['lead', 'senior', 'coauthor']).optional(),
    url: z.url().optional(),
    arxiv: z.string().regex(/^\d{4}\.\d{4,5}$/).optional(),
    scholarId: z.string().optional(),
    code: z.url().optional(),
    image: z.string().optional(),
    imageAlt: z.string().optional(),
    notes: z.array(z.string()).optional(),
    featured: z.boolean().optional(),
  }),
});

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: 'src/content/posts' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    draft: z.boolean().default(false),
    tags: z.array(z.string()).default([]),
  }),
});

export const collections = { publications, posts };
