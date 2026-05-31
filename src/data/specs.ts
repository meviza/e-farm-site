// E-Farm technical datasheet. Forward-looking figures are marked "target".

export type SpecRow = {
  group: string;
  label: string;
  value: string;
  note?: string;
};

export const specGroups = [
  "Vision / AI",
  "Perception",
  "Arm",
  "End-effector",
  "Mobility",
  "Power",
  "Connectivity",
  "Crops",
] as const;

export const specs: SpecRow[] = [
  // Vision / AI
  {
    group: "Vision / AI",
    label: "Vision model",
    value: "YOLOv8 (Ultralytics)",
    note: "trained via Roboflow",
  },
  {
    group: "Vision / AI",
    label: "Training data",
    value: "10,000+ labeled images",
    note: "5 crops",
  },
  {
    group: "Vision / AI",
    label: "Ripeness detection accuracy",
    value: "98%",
    note: "project test set",
  },
  // Perception
  {
    group: "Perception",
    label: "Depth sensing",
    value: "LiDAR + RGB-D fusion",
    note: "sub-cm localisation (target)",
  },
  // Arm
  {
    group: "Arm",
    label: "Manipulator",
    value: "6-axis arm, PAROL6-based (GPLv3)",
  },
  {
    group: "Arm",
    label: "Repeatability",
    value: "±0.1 mm class",
    note: "target",
  },
  {
    group: "Arm",
    label: "Reach / payload",
    value: "~440 mm / ~1 kg",
    note: "PAROL6 class",
  },
  // End-effector
  {
    group: "End-effector",
    label: "End-effector",
    value: "Adaptive force-controlled gripper",
    note: "SSG-48 / PincOpen-derived",
  },
  // Mobility
  {
    group: "Mobility",
    label: "Mobility",
    value: "Differential / rocker chassis",
    note: "NASA JPL OSR-derived",
  },
  // Power
  {
    group: "Power",
    label: "Power",
    value: "LiFePO4 pack + ESP32 BMS",
    note: "~8 h runtime (target)",
  },
  // Connectivity
  {
    group: "Connectivity",
    label: "Software",
    value: "ROS2 Humble, MQTT telemetry",
    note: "fleet + mobile apps",
  },
  // Crops
  {
    group: "Crops",
    label: "Crops",
    value: "Strawberry, tomato, pepper, cucumber, eggplant",
  },
];
