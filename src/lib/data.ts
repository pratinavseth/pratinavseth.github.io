// Loads and validates the YAML data files that aren't content collections.
// A malformed file fails the build with a clear message rather than rendering a broken page.
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { parse } from 'yaml';
import { z } from 'astro/zod';

function load<T extends z.ZodType>(name: string, schema: T): z.infer<T> {
  const raw = parse(readFileSync(join(process.cwd(), 'src/data', name), 'utf8'));
  const result = schema.safeParse(raw);
  if (!result.success) {
    throw new Error(`src/data/${name} is invalid:\n${z.prettifyError(result.error)}`);
  }
  return result.data;
}

const dated = z.object({ date: z.string().optional(), text: z.string() });
const photo = z.object({ src: z.string(), alt: z.string(), caption: z.string() });

export const news = load('news.yaml', z.array(z.object({ date: z.string(), text: z.string() })));

export const libraries = load(
  'libraries.yaml',
  z.array(
    z.object({
      name: z.string(),
      repo: z.string().regex(/^[\w.-]+\/[\w.-]+$/),
      url: z.url().optional(),
      paper: z.string().optional(),
      stars: z.number().int(),
      oss: z.boolean().default(false),
      role: z.string(),
      description: z.string(),
    }),
  ),
);

export const collaborators = load(
  'collaborators.yaml',
  z.record(
    z.string(),
    z.object({ institution: z.string(), role: z.enum(['manager', 'mentor', 'mentee', 'collaborator']) }),
  ),
);

export const experience = load(
  'experience.yaml',
  z.array(
    z.object({
      group: z.string(),
      roles: z.array(
        z.object({
          date: z.string(),
          role: z.string(),
          points: z.array(z.object({ label: z.string().optional(), text: z.string() })).default([]),
          papers: z.array(z.string()).default([]),
        }),
      ),
    }),
  ),
);

export const talks = load(
  'talks.yaml',
  z.object({
    upcoming: z.array(z.object({ name: z.string(), where: z.string(), when: z.string(), note: z.string() })).default([]),
    conferences: z.array(z.object({ name: z.string(), where: z.string(), note: z.string().optional() })),
    photos: z.array(photo),
    talks: z.array(z.object({ year: z.number(), items: z.array(dated) })),
    industry: z.array(dated),
  }),
);

export const education = load(
  'education.yaml',
  z.object({
    honors: z.array(dated),
    education: z.array(
      z.object({
        date: z.string(),
        degree: z.string(),
        school: z.string(),
        details: z.array(z.string()),
        photo: photo.optional(),
      }),
    ),
    service: z.object({
      mentoring: z.array(z.string()),
      mainConference: z.string(),
      workshops2026: z.array(z.string()),
      workshopsEarlier: z.array(z.string()),
    }),
    skills: z.array(z.object({ group: z.string(), items: z.array(z.string()) })),
    certifications: z.array(z.string()),
  }),
);

export const systems = load(
  'systems.yaml',
  z.object({
    title: z.string(),
    summary: z.string(),
    stages: z.array(
      z.object({
        step: z.string(),
        what: z.string(),
        tools: z.array(z.object({ name: z.string(), role: z.string(), paper: z.string().optional(), url: z.url().optional() })),
      }),
    ),
    loop: z.string(),
    principles: z.array(z.string()),
    keywords: z.array(z.string()),
  }),
);
