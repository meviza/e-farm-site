// Verified competitor landscape for autonomous fruit/vegetable harvesting robots.
// E-Farm's own row is flagged with isUs: true so the UI can highlight it.
// All figures sourced from public company disclosures and press as of 2025.

export type Competitor = {
  company: string;
  country: string;
  crops: string;
  tech: string;
  performance: string;
  funding: string;
  stage: string;
  isUs?: boolean;
};

export const competitors: Competitor[] = [
  {
    company: "MetoMotion GRoW",
    country: "Israel",
    crops: "Tomato, pepper, strawberry",
    tech: "3D vision + AI ripeness, dual-arm, 24/7",
    performance: "≥80% tomato-harvest labor cut",
    funding: "~$4.2M + EU H2020",
    stage: "Commercial pilots",
  },
  {
    company: "Tortuga AgTech",
    country: "USA",
    crops: "Strawberry, grape",
    tech: "Dual-arm CV/ML, robots-as-a-service",
    performance: "Gentle pick, quality preserved",
    funding: "$55M+ (acquired by Oishii 2025)",
    stage: "Acquired / scaling",
  },
  {
    company: "Four Growers GR-100",
    country: "USA",
    crops: "Tomato, cucumber",
    tech: "8 stereo cameras, AI ripeness, packing cart",
    performance: "98% ripe-selection accuracy",
    funding: "$15M+ ($9M Series A 2024)",
    stage: "Series A",
  },
  {
    company: "Octinion Rubion",
    country: "Belgium",
    crops: "Strawberry",
    tech: "Photonic RGB sensors, soft pick-from-below",
    performance: "360 kg/day vs ~50 kg/day human",
    funding: "n/a (undisclosed)",
    stage: "Commercial",
  },
  {
    company: "Agrobot E-Series",
    country: "Spain",
    crops: "Strawberry",
    tech: "ML ripeness + dual razor cutting",
    performance: "~20 acres / 3 days (claim)",
    funding: "Grants + Driscoll's",
    stage: "Commercial",
  },
  {
    company: "Saga Robotics Thorvald",
    country: "Norway",
    crops: "Strawberry, grapevine",
    tech: "Modular autonomous platform + UV-C",
    performance: "60–90% pesticide reduction",
    funding: "€9.5M (2025)",
    stage: "Series B",
  },
  {
    company: "FFRobotics",
    country: "Israel",
    crops: "Apple, citrus, stone fruit",
    tech: "Dual-finger gentle gripper",
    performance: "Field pilots (Washington)",
    funding: "Undisclosed + EU H2020",
    stage: "Pilot",
  },
  {
    company: "E-Farm",
    country: "Turkey",
    crops: "Strawberry, tomato, pepper, cucumber, eggplant",
    tech: "YOLOv8 (Roboflow, 10k+ imgs, 98%) + LiDAR depth + PAROL6 6-axis mm-precision arm + ESP32 BMS",
    performance: "98% ripeness detection (project test set)",
    funding: "Crowdfunding 2026",
    stage: "Prototype → pilot",
    isUs: true,
  },
];
