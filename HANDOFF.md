# Handoff: pratinavseth.github.io

State as of 19 Oct 2026. Live at https://pratinavseth.github.io, built from `dev-stable` by GitHub Actions.

## Current state

- The site is an **Astro 7 + TypeScript** rebuild of the old Jekyll site, live since 19 Oct 2026.
- `astro` and `dev-stable` point at the same commit and are what is live. `dev-stable` is now the repository's **default branch** (changed 24 Nov 2026), so the daily Scholar crawler and site rebuild run. `main` is the stale February 2025 Jekyll version.
- 24 Nov 2026: branch `polish-local` holds work that is **local only until the owner approves; do not push it without that.** It contains: the brick-wall headshot on the home page and share card; shorter paper `<title>` tags; a font preload (home layout shift on phone 0.23 to 0); smaller Talks photos; `llms.txt` with a current-role section and per-paper role labels; the draft post labelling under-review papers; arXiv ids for eight papers (CoReFusion, Orion-BiX, SafeTune, Provenance-Grounded Gating, LapGSR, SELF-PERCEPT, SSS at SemEval, RSM-NLP at BLP) with their abstracts; and a fix so `scripts/fetch-abstracts.mjs` no longer sends the owner's email address to arXiv. When the owner approves and it is pushed, change this bullet to say it is live.
- GitHub Pages source is **GitHub Actions** (`.github/workflows/deploy.yml`). Every push to `dev-stable` or `main` deploys in about 2 minutes.
- Last full check (24 Nov 2026): 0 type errors, 69 pages built, 22 rendered checks clean, no layout overflow at 1366px or 390px, 0 axe (WCAG A/AA) violations, every meta description 160 characters or fewer.

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

The system Node is 16, but Astro needs 22.22 or newer. **Install Node 22 LTS** (nodejs.org). Portable copies in temp folders get cleaned up: the one in the original handoff disappeared within a month.

```bash
npm install
npm run dev      # drafts visible
npm run build    # astro check + build
```

## Paper data and the CV

The Overleaf CV project (`bib/*.bib`, `notes/papers-status.md`, `notes/website-update.md`) is the source of truth for paper statuses, venues and authorship. `publications.yaml` was synced to it on 15 Nov 2026: 61 papers, 40 peer-reviewed, matching the CV. Deliberate differences: AgentTune is listed (not in the CV bibs), InterpSuite is not (internal name), and the Gemma 4 team report is listed as a team release.

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

1. **Papers without figures** (text tiles): the-off-switch-failure, document-as-function, brief, sailing-through-spectra, legalsearchgym, policy-grounded-insurance-agents, wording-risk-underwriting, evaluating-rule-adherence, directional-heterogeneity-multilingual-safety, mechanistic-flinch, three-steps-to-no. Needs the PDFs (none are on arXiv, and OpenReview blocks automation). Crop the main figure to `src/assets/images/<id>-fig.png` and set `image` and `imageAlt`. A figure-less paper can set `short:` for its tile label.
2. **Draft post** `what-survives-post-training.md` needs the owner's edit before setting `draft: false`. The Writing page is empty until then.
3. **GoatCounter:** set `goatcounter` in `site.ts` once the owner signs up.
4. **Paper coverage was checked on 24 Nov 2026** against alphaXiv (52 papers: 41 arXiv, 11 other) and Hugging Face (15): nothing is missing from the site. The eight arXiv ids above are not in the Overleaf `.bib` files yet, so add them at the next CV sync. arXiv's API rate-limits (HTTP 429); use the alphaXiv profile page instead.
5. **Search consoles:** verify in Google Search Console, submit `sitemap-index.xml`. Bing was pinged through IndexNow on 24 Nov (key file `public/da6fc9e7656707d8213521d90c4cb207.txt`); Bing Webmaster Tools verification is still open. Older profiles (ResearchGate, Linktree, alphaXiv, Stackforce, Scholar affiliation) still show old numbers and titles.
6. **Scholar crawler:** fixed on 15 Nov (`bibtexparser` pinned below 2, Python 3.12, 20-minute cap), but Google blocks GitHub's runners, so it mostly times out. Refresh `src/data/scholar-snapshot.json` from a local machine every month or so (`scholarly`, see `google_scholar_crawler/main.py`).
7. **Overleaf CV:** `resume.tex` line 138 still says "55+ submissions" for the Lexsi Hackathon; the site and the kit PDFs say 400+ (the owner's figure; the official hackathon page shows placeholder counters). The Overleaf git token in the owner's notes was rejected on 24 Nov (rotated); pull a fresh ZIP before the next sync.
8. **Not used from the media kit on purpose:** hiring and promo posters, QR codes, alternate logo crops, near-duplicate event photos, and the alignment-and-safety-stack diagram (it labels AlignTune "ICLR 2026 SPOT workshop", which is wrong; fix the label, then it can go on Experience).

## Outside this repo

- `Downloads\claude-resume-kit\MASTER-PROFILE.md` is the resume source of truth, generated from this repo's data. Regenerate it after data changes: `python regen_master_profile.py <repo path>` (in the same folder; regenerated 24 Nov 2026).
- `Downloads\claude-resume-kit\output\` holds `pratinav_seth_cv_full.pdf` (9 pages) and `pratinav_seth_cv_condensed.pdf` (2 pages), built from the Overleaf CV of 15 Nov 2026 (sources in `overleaf-2026-11-15\`). `website-copy\` is the same CV with the internal interpretability-library name replaced, and is what `public/files/` serves. The October resumes and `CRITIQUE.md` are in `archive-2026-10-19\`.
- Skills installed in `~/.claude/skills`: resume-tailoring, resume-tailoring-rs, resume-tailor-master-profile, humanizer, detect/remove/score-ai-slop, scientific-deslop, write-content, plus the earlier resume, SEO and GEO sets. `Downloads\resume-toolkit` and `Downloads\claude-resume-kit` are workspace kits; open Claude Code inside them to use their skills.

## Gotchas

- **Heredocs in this Windows shell drop backslashes** (for example `\t` in `\textbf`). Write Python or LaTeX edits to a file and run the file.
- **arXiv API rate-limits bursts.** `fetch-abstracts` falls back to reading individual pages 3 seconds apart.
- **OpenReview requires a human browser check**, even in a headed Playwright browser.
- **Port 4321 may be taken** by another local Astro preview (the banquet site), so preview may land on 4322.
- **The antislop skills** need `skills/remove-ai-slop/references/` inside each installed skill folder, or the counter silently finds nothing.
- **The portable Node folder in a session scratchpad can be cleaned mid-session** (npm's files disappear, `node.exe` stays). `node node_modules/astro/bin/astro.mjs build` still works without npm.
- **`bibtex` must run on every multibib group** (`for a in $(grep -l bibdata *.aux)`), not just `resume.aux`, or the full CV builds with 60+ undefined citations.
