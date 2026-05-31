// Peer-reviewed and preprint literature contextualising E-Farm's approach.
// These are EXTERNAL references — not E-Farm's own results.

export type Reference = {
  authors: string;
  year: number;
  title: string;
  venue: string;
  url: string;
};

export const references: Reference[] = [
  {
    authors: "Wang, C. et al.",
    year: 2024,
    title: "Strawberry Detection and Ripeness Classification Using YOLOv8+ Model",
    venue: "Agriculture 14(5):751",
    url: "https://doi.org/10.3390/agriculture14050751",
  },
  {
    authors: "Xiao, B., Nguyen, M., Yan, W.Q.",
    year: 2024,
    title: "Fruit Ripeness Identification Using YOLOv8",
    venue: "Multimedia Tools and Applications 83:28039–28056",
    url: "https://doi.org/10.1007/s11042-023-16570-9",
  },
  {
    authors: "Kang, H., Wang, X., Chen, C.",
    year: 2022,
    title:
      "Accurate Fruit Localisation for Robotic Harvesting using High-Resolution LiDAR-Camera Fusion",
    venue: "arXiv:2205.00404",
    url: "https://arxiv.org/abs/2205.00404",
  },
  {
    authors: "Farhan, S.M. et al.",
    year: 2024,
    title:
      "A Comprehensive Review of LiDAR Applications in Crop Management for Precision Agriculture",
    venue: "Sensors 24(16):5409",
    url: "https://doi.org/10.3390/s24165409",
  },
  {
    authors: "Rajendran, V. et al.",
    year: 2024,
    title:
      "Towards Autonomous Selective Harvesting: A Review of Robot Perception, Design, Motion Planning and Control",
    venue: "Journal of Field Robotics 41:2247–2279",
    url: "https://doi.org/10.1002/rob.22230",
  },
  {
    authors: "Parsa, S. et al.",
    year: 2024,
    title: "Modular Autonomous Strawberry Picking Robotic System",
    venue: "Journal of Field Robotics 41:2226–2246",
    url: "https://doi.org/10.1002/rob.22229",
  },
  {
    authors: "Lehnert, C. et al.",
    year: 2017,
    title: "Autonomous Sweet Pepper Harvesting for Protected Cropping Systems",
    venue: "arXiv:1706.02023",
    url: "https://arxiv.org/abs/1706.02023",
  },
  {
    authors: "Li, X. et al.",
    year: 2024,
    title:
      "AHPPEBot: Autonomous Robot for Tomato Harvesting based on Phenotyping and Pose Estimation",
    venue: "IEEE ICRA 2024 (arXiv:2405.06959)",
    url: "https://arxiv.org/abs/2405.06959",
  },
];
