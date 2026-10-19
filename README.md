# pratinavseth.github.io

Source for [pratinavseth.github.io](https://pratinavseth.github.io), built with [Astro](https://astro.build) and TypeScript.

Every number on the site (paper counts, peer-reviewed count, collaborator counts, citations, GitHub stars) is computed from the data files at build time. Nothing is hand-typed in the pages, so nothing can drift.

## Where things live

| To change… | Edit |
|---|---|
| Papers (title, authors, venue, status, links, figure) | `src/data/publications.yaml` |
| Paper abstracts | `src/data/abstracts.json` (filled by `npm run fetch:abstracts`) |
| News feed | `src/data/news.yaml` |
| Experience | `src/data/experience.yaml` |
| Talks, events, conference photos | `src/data/talks.yaml` |
| Education, honours, reviewing, skills | `src/data/education.yaml` |
| Libraries and their GitHub repos | `src/data/libraries.yaml` |
| Who each co-author is (mentee, manager…) | `src/data/collaborators.yaml` |
| The three bios on the home page | `src/data/bio/*.md` (`{peerReviewed}`, `{citations}`, `{stars}` are filled in automatically) |
| Name, email, links, "open to", analytics | `src/config/site.ts` |
| Blog posts | `src/content/posts/*.md` (set `draft: false` to publish) |
| Figures and photos | `src/assets/images/` (resized and converted automatically) |
| CV PDFs | `public/files/` |

## Adding a paper

1. Add an entry to `src/data/publications.yaml`, near the top of its area. Use `status: published` only for papers accepted at a peer-reviewed venue.
2. If it has an arXiv id, run `npm run fetch:abstracts` to pull its abstract.
3. Put a figure in `src/assets/images/` and set `image:` to its file name.
4. If a co-author is new, add them to `src/data/collaborators.yaml` (the build warns if you forget).

The build fails with a clear message if a field is missing or misspelled.

## Running locally

Requires Node 22.22 or newer.

```bash
npm install
npm run dev        # http://localhost:4321, shows draft posts
npm run build      # type-check + production build into dist/
OFFLINE=1 npm run build   # skip fetching live citations/stars
```

## Deployment

`.github/workflows/deploy.yml` builds and deploys on every push to `dev-stable` or `main`, and once a day so citations and stars stay current. In the repository settings, **Pages → Source** must be **GitHub Actions**.

Citations come from the `google-scholar-stats` branch, written daily by `.github/workflows/google_scholar_crawler.yaml` (needs the `GOOGLE_SCHOLAR_ID` secret). If that data can't be fetched, the build uses `src/data/scholar-snapshot.json`.

## Analytics

Set `goatcounter` in `src/config/site.ts` to your GoatCounter site code to turn on privacy-friendly analytics (no cookies).
