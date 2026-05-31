// Program roadmap. Items from 2025 onward are forward-looking targets.

export type Milestone = {
  year: string;
  title: string;
  description: string;
  target?: boolean;
};

export const roadmap: Milestone[] = [
  {
    year: "2022",
    title: "Founded",
    description:
      "E-Farm established at Gebze Bilişim Vadisi (Informatics Valley), Turkey — a multidisciplinary team forms around autonomous greenhouse harvesting.",
  },
  {
    year: "2023",
    title: "Vision model",
    description:
      "YOLOv8 detection/ripeness model trained on 10,000+ labeled images via Roboflow, reaching 98% accuracy on the project test set across 5 crops.",
  },
  {
    year: "2024",
    title: "Arm integration & LiDAR fusion",
    description:
      "Integration of the PAROL6 6-axis manipulator with LiDAR + RGB-D depth fusion for sub-centimetre fruit localisation.",
  },
  {
    year: "2025",
    title: "Greenhouse pilot",
    description:
      "First in-greenhouse pilot runs validating the full Detect → Localize → Grasp → Deposit pipeline under production row conditions.",
    target: true,
  },
  {
    year: "2026",
    title: "Crowdfunding & pre-series",
    description:
      "Public crowdfunding campaign and pre-series production to fund the first commercial robot batch.",
    target: true,
  },
  {
    year: "2027",
    title: "Fleet rollout",
    description:
      "Multi-robot fleet deployments with fleet-management software, telemetry and remote support at scale.",
    target: true,
  },
];
