import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://artofsmallsteps.com',
  // Half-built pages taken down before the Meta ads (web-campaign session, 2026-11-22).
  redirects: {
    '/method': '/wayfinder-method/',
    '/program': '/wayfinder-method/',
    '/about': '/',
  },
});
