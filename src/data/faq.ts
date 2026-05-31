// Honest backer FAQ. Prose lives in the locale JSON; this file only fixes the
// key order so sections/Faq.astro can iterate deterministically.

export const faqKeys = [
  "crops",
  "accuracy",
  "delivery",
  "opensource",
  "safety",
  "refund",
  "privacy",
  "reservation",
] as const;

export type FaqKey = (typeof faqKeys)[number];
