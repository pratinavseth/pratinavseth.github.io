# Pratinav Seth — Research Website

This repository contains the source for [pratinavseth.github.io](https://pratinavseth.github.io), a Jekyll site for Pratinav Seth's research, publications, experience, talks, education, and academic service.

## Site pages

- `_pages/about.md` — biography, selected work, and news
- `_pages/publications.md` — publications, preprints, and research libraries
- `_pages/experience.md` — professional and research experience
- `_pages/talks-events.md` — talks, conferences, and industry events
- `_pages/education-service.md` — education, honors, reviewing, skills, and collaborators

Navigation is configured in `_data/navigation.yml`; site identity and Jekyll settings are in `_config.yml`.

## Local development

Install Ruby and Bundler, then install the dependencies and start Jekyll:

```sh
bundle install
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000`. Changes to `_config.yml` require restarting the server.

The Google Scholar citation crawler and its scheduled GitHub Actions workflow are in `google_scholar_crawler/` and `.github/workflows/`. The workflow requires the `GOOGLE_SCHOLAR_ID` repository secret and writes generated citation data to the `google-scholar-stats` branch.

## Credits

The site began with the [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) theme and also draws on work from [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) and [Academic Pages](https://github.com/academicpages/academicpages.github.io). See [LICENSE](LICENSE) for licensing details.
