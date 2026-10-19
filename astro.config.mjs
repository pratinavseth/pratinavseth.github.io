// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://pratinavseth.github.io',
  trailingSlash: 'always',
  // Old Jekyll addresses that other sites may still link to.
  redirects: {
    '/about/': '/',
    '/education/': '/education-service/',
    '/service-skills/': '/education-service/',
  },
  integrations: [sitemap({ filter: (page) => !page.includes('/404') })],
  image: {
    responsiveStyles: true,
  },
});
