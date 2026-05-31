# 🌱 E-Farm — Crowdfunding Landing Site

Single-page marketing/crowdfunding site for **E-Farm**, an autonomous greenhouse
fruit-harvesting robot. Built with **Astro 6 + React 19 + Tailwind v4**, deployed
to GitHub Pages.

Production URL: `https://meviza.github.io/e-farm-site/`

## Develop

```sh
npm install
npm run dev        # http://localhost:4321/e-farm-site/
```

## Build & preview

```sh
npm run build      # → ./dist
npm run preview
```

The build emits a static, fully pre-rendered site:

```
dist/index.html        # English (default locale, served at /)
dist/de/index.html     # German
dist/fr/index.html     # French
dist/es/index.html     # Spanish
dist/it/index.html     # Italian
dist/nl/index.html     # Dutch
dist/tr/index.html     # Turkish
dist/.nojekyll         # required for GitHub Pages
```

## Internationalisation

- Locales: `en` (default, at `/`), `de`, `fr`, `es`, `it`, `nl`, `tr` (path-prefixed).
- All user-facing copy lives in `src/i18n/locales/*.json`.
- **`en.json` is the source of truth.** The other six JSON files are placeholders;
  `useTranslations()` (in `src/i18n/ui.ts`) **falls back to English** for any missing
  key, so the site is fully functional before translation. To localise a language,
  copy keys from `en.json` into the matching file and translate the values.

## Formspree (reservation form)

The grower reservation form posts to Formspree. Set your form id in:

```
src/components/sections/Reservation.astro
```

Replace `REPLACE_FORM_ID` in:

```ts
const endpoint = "https://formspree.io/f/REPLACE_FORM_ID";
```

Submissions go straight to the E-Farm team. A hidden `_gotcha` honeypot guards
against spam.

## Images & downloads

Drop assets into `public/` (served from the `/e-farm-site/` base):

- `public/images/renders/hero.webp` — hero render. If absent, the hero shows a
  styled fallback box automatically (no broken image).
- `public/downloads/` — backer documents: `whitepaper.pdf`, `datasheet.pdf`,
  `press-kit.zip`, `term-sheet.pdf`, `parol6-manual.pdf`. The Resources section
  links them whether or not the files exist yet; flip a resource's `ready` flag in
  `src/components/sections/Resources.astro` once a file is added.

## Theming

Light/dark is token-driven via CSS variables in `src/styles/global.css` and a
no-flash inline script in `BaseLayout.astro`. The `ThemeToggle` island persists
the choice to `localStorage`.

## Deploy (GitHub Pages)

Pushing to `main` triggers `.github/workflows/deploy.yml`
(`withastro/action@v3` → `actions/deploy-pages@v4`).

**One-time setup:** in the repo, go to **Settings → Pages → Build and deployment →
Source** and select **GitHub Actions**.

## Project structure

```
src/
├── components/
│   ├── Nav.astro, LangSwitcher.astro, Reveal.tsx
│   ├── islands/       # React: ThemeToggle, CompetitorMatrix, MarketChart,
│   │                  #        FaqAccordion, ReservationForm
│   └── sections/      # one .astro per page section
├── data/              # competitors, references, specs, tiers, roadmap, faq
├── i18n/              # ui.ts + locales/*.json
├── layouts/BaseLayout.astro
├── pages/             # index.astro (en) + [lang]/index.astro (6 locales)
└── styles/global.css
```
