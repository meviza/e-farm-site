// i18n helpers for a fully static, multi-locale Astro site.
// English is the default (served at /), other locales are path-prefixed (/de/, /tr/, …).
import en from "./locales/en.json";
import de from "./locales/de.json";
import fr from "./locales/fr.json";
import es from "./locales/es.json";
import it from "./locales/it.json";
import nl from "./locales/nl.json";
import tr from "./locales/tr.json";

export const languages = {
  en: "English",
  de: "Deutsch",
  fr: "Français",
  es: "Español",
  it: "Italiano",
  nl: "Nederlands",
  tr: "Türkçe",
} as const;

export type Lang = keyof typeof languages;
export const defaultLang: Lang = "en";

const dictionaries: Record<Lang, Record<string, unknown>> = {
  en,
  de,
  fr,
  es,
  it,
  nl,
  tr,
};

/** Derive the active locale from the URL path; falls back to English. */
export function getLangFromUrl(url: URL): Lang {
  const [, maybeLang] = url.pathname.replace(/^\/e-farm-site/, "").split("/");
  if (maybeLang && maybeLang in languages) return maybeLang as Lang;
  return defaultLang;
}

function lookup(dict: Record<string, unknown>, key: string): string | undefined {
  return key.split(".").reduce<unknown>((acc, part) => {
    if (acc && typeof acc === "object" && part in (acc as Record<string, unknown>)) {
      return (acc as Record<string, unknown>)[part];
    }
    return undefined;
  }, dict) as string | undefined;
}

/** Returns a translator that falls back to English, then to the raw key. */
export function useTranslations(lang: Lang) {
  return function t(key: string): string {
    return lookup(dictionaries[lang], key) ?? lookup(dictionaries[defaultLang], key) ?? key;
  };
}

/** Build a locale-aware path (keeps the GitHub Pages base prefix out of callers). */
export function localizedPath(lang: Lang, path = ""): string {
  const clean = path.replace(/^\//, "");
  if (lang === defaultLang) return `/${clean}`;
  return `/${lang}/${clean}`;
}
