# Handoff: pratinavseth.github.io

State as of 19 Oct 2026. Live at https://pratinavseth.github.io, built from `dev-stable` by GitHub Actions.

## Current state

- The site is an **Astro 7 + TypeScript** rebuild of the old Jekyll site, live since 19 Oct 2026.
- `astro` and `dev-stable` point at the same commit. `main` is the stale February 2025 Jekyll version and is still the repository's **default branch** (see Open items).
- GitHub Pages source is **GitHub Actions** (`.github/workflows/deploy.yml`). Every push to `dev-stable` or `main` deploys in about 2 minutes.
- Last full check: 0 type errors, 61 pages, no layout overflow at 1366px or 390px, 0 axe (WCAG A/AA) violations, every meta description 160 characters or fewer.

## How it works

Everything on the site is generated from data files. Pages never hand-type a number.

| To change | Edit |
|---|---|
| Papers | `src/data/publications.yaml` (validated by `src/content.config.ts`; a bad field fails the build) |
| Abstracts | `src/data/abstracts.json` (`npm run fetch:abstracts`) |
| Experience roles | `src/data/experience.yaml` (`theme` = bold one-liner; text may use `{stars}`, `{libraryCount}`) |
| Stack diagram on Experience | `src/data/systems.yaml` |
| Libraries (logo, role, repo) | `src/data/libraries.yaml` |
| News, talks, education | `news.yaml`, `talks.yaml`, `education.yaml` |
| Collaborator roles | `src/data/collaborators.yaml` (counts come from papers) |
| Bios | `src/data/bio/*.md` (`{peerReviewed}`, `{citations}`, `{stars}` filled at build) |
| Name, links, analytics | `src/config/site.ts` |
| Blog | `src/content/posts/*.md` (`draft: true` hides it from the live site and the menu) |
| Figures and logos | `src/assets/images/` (Astro resizes them to WebP) |

At build time:
- **Citations** come from the `google-scholar-stats` branch, falling back to `src/data/scholar-snapshot.json`.
- **GitHub stars** come from the API, falling back to the numbers in `libraries.yaml`.
- `OFFLINE=1 npm run build` skips both fetches.

Every paper gets its own page with Google Scholar `citation_*` tags, ScholarlyArticle JSON-LD, BibTeX and a 1200×630 share image. `llms.txt` and the sitemap are generated too.

## Running locally

The system Node is 16, but Astro needs 22.22 or newer. Either install Node 22 LTS, or use the portable copy:

```bash
export PATH="/c/Users/prati/AppData/Local/Temp/claude/c--Users-prati-Downloads-rsbnq-github-io/ee548074-2581-44dd-8aa5-e4993d2a82f5/scratchpad/node/node-v22.23.3-win-x64:$PATH"
npm install
npm run dev      # drafts visible
npm run build    # astro check + build
```

That portable path is in a temp folder and may disappear. Installing Node 22 is the durable fix.

## Decisions the owner made (keep them)

- **Design:** keep the original identity (paper `#f4f4f0`, ink, hazard red `#e61919`, square corners, Archivo Black / IBM Plex Sans / JetBrains Mono) with an editorial hero and data-led sections.
- **Pitch:** "Trustworthy AI, from the data to the deployed agent". Current focus is safety, alignment, interpretability and agents. Tabular foundation models and the climate, medical, NLP and vision work sit under "earlier research".
- **Calls to action:** "research collaborations" and "talks" are stated openly. Jobs and advising are only implied. Contact is email plus LinkedIn.
- **Never name internal tools.** Write "pruning library", "quantization library", "post-hoc interpretability library" and "internal AI coding-agent platform". No client or regulator names; describe domains only.
- **`myRole` on papers:** `lead` = first author or main hands-on contributor; `senior` = mentored the first author or led the design. The owner confirmed every value.
- **Library roles** were confirmed by the owner and are listed in `libraries.yaml`. They must match `systems.yaml` and `experience.yaml`.
- **Writing:** US spelling (paper titles stay as published), no em-dashes, no filler words, no invented claims about the owner.
- **Process:** the owner prefers decisions asked one question at a time, with a recommended option.

## Open items

1. **Make `dev-stable` the default branch** (Settings → General). Scheduled workflows only run on the default branch, so the Scholar crawler and the daily rebuild are idle and citations are frozen at 2026-09-01.
2. **Four papers still use title placeholders:** the-off-switch-failure, document-as-function, brief, sailing-through-spectra. None are on arXiv, and OpenReview blocks automated downloads. Save the PDFs and crop Figure 1.
3. **Draft post** `what-survives-post-training.md` needs the owner's edit before setting `draft: false`.
4. **GoatCounter:** set `goatcounter` in `site.ts` once the owner signs up.
5. **Search consoles:** verify in Google Search Console and Bing Webmaster Tools, submit `sitemap-index.xml`, and link the site from Scholar, LinkedIn, GitHub, ORCID and X.
6. **Scholar crawler** has been failing intermittently since August, probably because Google Scholar blocks GitHub's runners. Check the Actions logs after item 1.

## Outside this repo

- `Downloads\claude-resume-kit\MASTER-PROFILE.md` is the resume source of truth, generated from this repo's data. Regenerate it after data changes.
- `Downloads\claude-resume-kit\output\` holds the research and tech-lead resumes (2-page LaTeX and PDF) and `CRITIQUE.md`, which lists the evidence to add before sending.
- Skills installed in `~/.claude/skills`: resume-tailoring, resume-tailoring-rs, resume-tailor-master-profile, humanizer, detect/remove/score-ai-slop, scientific-deslop, write-content, plus the earlier resume, SEO and GEO sets. `Downloads\resume-toolkit` and `Downloads\claude-resume-kit` are workspace kits; open Claude Code inside them to use their skills.

## Gotchas

- **Heredocs in this Windows shell drop backslashes** (for example `\t` in `\textbf`). Write Python or LaTeX edits to a file and run the file.
- **arXiv API rate-limits bursts.** `fetch-abstracts` falls back to reading individual pages 3 seconds apart.
- **OpenReview requires a human browser check**, even in a headed Playwright browser.
- **Port 4321 may be taken** by another local Astro preview (the banquet site), so preview may land on 4322.
- **The antislop skills** need `skills/remove-ai-slop/references/` inside each installed skill folder, or the counter silently finds nothing.
