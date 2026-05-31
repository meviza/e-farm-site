// Pledge tiers. ALL prices are illustrative / target figures for the campaign.

export type Tier = {
  name: string;
  price: string;
  limit?: string;
  includes: string[];
  featured?: boolean;
};

export const tiers: Tier[] = [
  {
    name: "Supporter",
    price: "€25",
    includes: [
      "Name in backers list",
      "Digital whitepaper + datasheet",
      "Developer progress updates",
    ],
  },
  {
    name: "Early-Bird Pilot",
    price: "€19,900",
    limit: "Limited to 25",
    featured: true,
    includes: [
      "Early production slot",
      "~15% off list price",
      "Lifetime software updates",
    ],
  },
  {
    name: "Core Robot",
    price: "€23,900",
    includes: [
      "Full E-Farm robot",
      "Standard support",
      "Software updates",
    ],
  },
  {
    name: "Deluxe Deployment",
    price: "€31,900",
    includes: [
      "Robot + priority deployment",
      "On-site setup & commissioning",
      "2-year support",
    ],
  },
  {
    name: "Commercial Fleet",
    price: "€110,000",
    limit: "Limited",
    includes: [
      "5-robot fleet",
      "Fleet-management software",
      "Dedicated support engineer",
    ],
  },
  {
    name: "Founder's Circle",
    price: "€149,000",
    limit: "5–10 only",
    includes: [
      "Robot + naming recognition",
      "Monthly progress calls",
      "Direct line to the engineering team",
    ],
  },
];
