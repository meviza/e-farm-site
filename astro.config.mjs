// @ts-check
import { defineConfig } from "astro/config";
import react from "@astrojs/react";
import tailwindcss from "@tailwindcss/vite";

// E-Farm crowdfunding landing site.
// Deployed to GitHub Pages project site: https://meviza.github.io/e-farm-site/
export default defineConfig({
  site: "https://meviza.github.io",
  base: "/e-farm-site",
  trailingSlash: "ignore",
  integrations: [react()],
  vite: {
    plugins: [tailwindcss()],
  },
  i18n: {
    defaultLocale: "en",
    locales: ["en", "de", "fr", "es", "it", "nl", "tr"],
    routing: {
      prefixDefaultLocale: false,
    },
  },
});
