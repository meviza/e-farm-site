<!--
SPDX-FileCopyrightText: 2022-2026 E-Farm Robotics <hello@efarm.dev>
SPDX-License-Identifier: CC-BY-4.0

READY-TO-PASTE BACKERKIT CAMPAIGN COPY.
Paste each section into the matching BackerKit campaign field. All forward-looking
figures are labelled as targets/estimates. Replace bracketed [PLACEHOLDERS] before
publishing. Default language: English (translate per BackerKit locale settings).
-->

# 🍓🤖 E-Farm — The Open Autonomous Greenhouse Harvesting Robot

> **Tagline:** Autonomous greenhouse harvesting, engineered openly.

> **One-liner (for the BackerKit header):** A computer-vision + robotic-arm platform that finds ripe fruit and picks it with millimetre precision — built on open source, priced for real growers.

---

## ⚡ The 30-second pitch

Greenhouses can grow the food — but they increasingly **can't find the people to pick it**. E-Farm is an autonomous robot that drives a greenhouse row, **detects ripe fruit with a 98%-accuracy computer-vision model** (YOLOv8, trained on 10,000+ images across 5 crops), measures exactly where each fruit is with a **LiDAR + depth camera**, and harvests it with a **6-axis robotic arm** built on the open-source PAROL6 platform.

We've spent **three years (since 2022, at Gebze Bilişim Vadisi / Informatics Valley, Türkiye)** turning that idea from a vision model into an integrated machine. Now we're inviting growers, engineers and supporters to help us get from working prototype to first field fleet — **in the open**, with our entire software/hardware stack public on GitHub.

---

## 🌍 The problem: the harvest-labour gap

Picking is the single most labour-intensive task in protected horticulture, and the workforce is shrinking:

- The EU lost the equivalent of **~3.5 million full-time farm workers between 2009 and 2024**.
- Only **~11% of EU farms** are run by people under 40 — the pipeline is thin.
- In the US, an estimated **2.4 million agricultural jobs** go unfilled and **56% of farmers report labour shortages**.
- The greenhouses are there to serve: **Türkiye ~77,600 ha** (Antalya alone ~31,600 ha — 46% of the national total), **Netherlands ~10,260 ha**, **Spain ~76,600 ha** (Almería ~40,000 ha).

Fruit that isn't picked on time is fruit that's lost. Growers need a picker that shows up every day.

---

## 🤖 What E-Farm does

A single robot performs the full selective-harvest cycle, autonomously:

1. **Detect** 🫐 — A YOLOv8 vision model (trained via Roboflow on 10,000+ labelled images, 5 crops) identifies fruit and classifies ripeness at **98% accuracy on our test set**.
2. **Localise** 📐 — A LiDAR + RGB-D camera fuses colour and depth to pinpoint each ripe fruit in 3D (sub-centimetre localisation is our engineering target, consistent with published LiDAR-camera fusion results).
3. **Pick** 🦾 — A 6-axis arm (built on the open-source **PAROL6**, GPLv3) approaches with a force-controlled adaptive gripper and detaches the fruit gently.
4. **Report** 📡 — Every robot streams telemetry over MQTT to a web fleet dashboard and a mobile app, so a grower can manage many robots from a phone.

Crops at launch: **strawberry, tomato, pepper, cucumber, eggplant.**

---

## 🔬 Why you can believe us

We're deliberately not promising magic. Here's our evidence base:

- **It's open source.** Our entire stack — perception, manipulation (ROS 2), embedded/BMS firmware, IoT, the ML training pipeline, the fleet web dashboard and mobile app — is public and tested: **[github.com/meviza/E-Farm-Autonomous-Harvesting-Robot](https://github.com/meviza/E-Farm-Autonomous-Harvesting-Robot)**. Anyone can inspect exactly how it works.
- **We build on proven open hardware.** The arm derives from the open-source **PAROL6** 6-axis design; the chassis takes cues from **NASA JPL's Open Source Rover**; battery management is informed by **foxBMS**. We attribute and license everything correctly.
- **The science is real.** Peer-reviewed work backs every subsystem — e.g. YOLOv8 ripeness classification at 97.8–99.5% accuracy (Wang et al. 2024; Xiao et al. 2024), LiDAR-camera fruit localisation to ~0.25 cm (Kang et al. 2022), and full greenhouse harvesting robots reaching ~86% pick success (Li et al., ICRA 2024). Full reference list on our site and in the whitepaper.
- **We know the field.** Commercial peers (MetoMotion, Four Growers, Tortuga, Octinion, Agrobot, Saga, FFRobotics) prove the market is real and fundable. Our wedge: **multi-crop greenhouses, an open stack, and a price built for everyday growers — from Türkiye outward.**

---

## 👥 The team

E-Farm was founded in 2022 at **Gebze Bilişim Vadisi (Informatics Valley)**, Türkiye, by a **five-person multidisciplinary team** spanning computer vision, robotics, embedded systems, mechanical design and software — with prior start-up and engineering experience. We're keeping this campaign about the machine, not the founders' CVs; what matters is three years of focused, documented R&D you can read on GitHub.

---

## 🗺️ Roadmap

| When | Milestone | Status |
|------|-----------|--------|
| 2022 | Company founded; problem & crop selection | ✅ Done |
| 2023 | Vision model: YOLOv8, 10k+ images, 98% | ✅ Done |
| 2024 | Arm integration (PAROL6) + LiDAR depth fusion | ✅ Done |
| 2025 | Greenhouse pilot & field data | 🎯 Target |
| **2026** | **Crowdfunding + pre-series build** | 🚀 This campaign |
| 2027 | First grower fleet rollout | 🎯 Target |

---

## 💚 Reward tiers

> All prices are **illustrative campaign targets** and will be confirmed at launch. Hardware tiers include lifetime access to our open-source software updates.

| Tier | Pledge | Limit | What you get |
|------|--------|-------|--------------|
| **Supporter** | €25 | — | Your name in our backers wall, the digital whitepaper + datasheet, and dev-log updates. Fund the mission. |
| **Early-Bird Pilot** 🐦 | €19,900 | 25 | One robot at the best price (~15% off Core), an early production slot, and lifetime software updates. |
| **Core Robot** | €23,900 | — | One full E-Farm robot, standard support, and software updates. The everyday-grower tier. |
| **Deluxe Deployment** | €31,900 | — | Robot + priority production + **on-site setup & calibration** + 2 years of support. |
| **Commercial Fleet** | €110,000 | limited | **5-robot fleet** + the fleet-management dashboard + a dedicated support contact. |
| **Founder's Circle** | €149,000 | 5–10 | A robot + naming recognition in the project + monthly progress calls with the team. |

---

## 🎯 Stretch goals

- **+ Cucumber & pepper firmware pack** — unlock additional crop models for every backer.
- **+ Cloud analytics dashboard** — yield forecasting & harvest heatmaps, free for the first year.
- **+ Multilingual grower support** — documentation & UI in EN/DE/FR/ES/IT/NL/TR (already scaffolded on our site).
- **+ Open hardware day** — we publish an additional reference end-effector design under an open licence.

---

## 💸 Where your money goes

| Allocation | Share (target) |
|------------|----------------|
| Hardware & manufacturing (arm, sensors, chassis, BMS, gripper) | ~45% |
| Engineering & integration (perception, ROS 2, firmware) | ~25% |
| Field pilots, safety testing & certification path (CE) | ~15% |
| Fulfilment, logistics & support | ~10% |
| Platform/contingency | ~5% |

---

## ⚠️ Risks & challenges (read this)

We'd rather be honest than optimistic:

- **Hardware timelines slip.** Electronics sourcing and mechanical iteration are unpredictable. Our stated delivery windows are deliberately conservative, and we'll communicate any change early and on the platform.
- **Field performance ≠ lab performance.** Our 98% figure is ripeness *detection* accuracy on our test set; end-to-end *pick* success in a live canopy is lower and is exactly what our 2025 pilot is for. Published greenhouse robots report ~86% pick success — that's the honest neighbourhood.
- **Safety & compliance.** A moving robotic arm around people requires real safety engineering and a CE-marking path; part of the raise funds exactly this. We will not ship without third-party safety testing.
- **We're a small team.** Five people, three years in. The open-source stack is our hedge: if you back us, the work stays public and auditable no matter what.

---

## ❓ FAQ

**Which crops does it support?** Strawberry, tomato, pepper, cucumber and eggplant at launch; more via firmware updates and stretch goals.

**What does "98% accuracy" actually mean?** It's the accuracy of our ripeness-detection vision model on a held-out test set — not a guarantee of pick success in every greenhouse. See the Risks section.

**Why open source?** Trust and longevity. Growers and researchers can verify, extend and maintain the platform; it also lets us build on excellent existing work (PAROL6, MoveIt 2, ROS 2, RealSense, foxBMS) and give credit properly.

**When will I receive my robot?** Hardware tiers target shipment after the 2025–2026 pilot and pre-series build; exact windows confirmed at campaign launch. We under-promise on timing.

**Can I cancel / get a refund?** Yes — per BackerKit's pledge terms and our published term sheet (downloadable on our site). Pre-production pledges can be cancelled before the production lock date.

**How is my reservation data handled?** Company reservations reach our team directly and are used only to coordinate your pledge. We don't sell data.

**I'm a researcher / developer — can I contribute?** Please do. The repo has good-first-issues, a contribution guide, and a clean multi-package architecture.

---

## 🔗 Links

- 🌐 **Landing page:** https://meviza.github.io/e-farm-site/
- 💻 **Open-source code:** https://github.com/meviza/E-Farm-Autonomous-Harvesting-Robot
- 📄 **Downloads:** Whitepaper · Technical datasheet · Term sheet (on the landing page)
- ✉️ **Contact / grower reservations:** via the reservation form on the landing page

> *E-Farm is an engineering-stage project. We show prototypes and illustrative renders, label targets as targets, and publish our work openly. Thank you for helping bring an open harvesting robot to real greenhouses.* 🌱
