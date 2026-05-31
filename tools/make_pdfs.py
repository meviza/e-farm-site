# SPDX-License-Identifier: MIT
"""
make_pdfs.py - Generate branded backer-resource PDFs for the E-Farm crowdfunding campaign.

Produces three documents into ../public/downloads/:
  1. efarm-whitepaper.pdf   - Technical Overview & Vision (~5-7 pages)
  2. efarm-datasheet.pdf     - Technical datasheet (1-2 pages)
  3. efarm-term-sheet.pdf    - Crowdfunding pledge / term sheet (1-2 pages)

Pure-Python (fpdf2) so it works without system PDF tooling:
    python3 -m venv /tmp/venv_pdf
    /tmp/venv_pdf/bin/pip install fpdf2
    /tmp/venv_pdf/bin/python tools/make_pdfs.py

Content is real (sourced figures, real DOIs/arXiv ids). Figures that are forward
-looking are explicitly labelled "target" or "illustrative".
"""

import os
import sys

from fpdf import FPDF

# --------------------------------------------------------------------------- #
# Brand constants
# --------------------------------------------------------------------------- #
GREEN = (31, 122, 68)        # E-Farm primary accent #1f7a44
GREEN_DARK = (20, 84, 47)
GREEN_LIGHT = (233, 244, 237)
INK = (33, 41, 38)
GREY = (110, 120, 116)
LINE = (210, 218, 213)
WHITE = (255, 255, 255)

PROJECT_URL = "github.com/meviza/E-Farm-Autonomous-Harvesting-Robot"
SITE = "e-farm.org"  # campaign/site reference
YEAR = "2026"
VERSION = "v1.0"

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.normpath(os.path.join(HERE, "..", "public", "downloads"))

# Find a Unicode-capable TTF so the euro sign and special chars render.
UNICODE_FONT_CANDIDATES = [
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans.ttf",
]
UNICODE_FONT = next((p for p in UNICODE_FONT_CANDIDATES if os.path.exists(p)), None)


# --------------------------------------------------------------------------- #
# Base PDF with shared branding helpers
# --------------------------------------------------------------------------- #
class EFarmPDF(FPDF):
    def __init__(self, doc_title, doc_sub):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.doc_title = doc_title
        self.doc_sub = doc_sub
        self.unicode = False
        self.base = "Helvetica"
        self.set_auto_page_break(auto=True, margin=20)
        self.set_margins(18, 18, 18)
        if UNICODE_FONT:
            try:
                self.add_font("EF", "", UNICODE_FONT)
                # Reuse the same TTF for the bold slot; we emphasise with size/colour.
                self.add_font("EF", "B", UNICODE_FONT)
                self.base = "EF"
                self.unicode = True
            except Exception:
                self.base = "Helvetica"
                self.unicode = False
        self._draw_header_footer = True

    # ---- text-safety: strip chars the core fonts cannot encode (latin-1) ---- #
    def t(self, s):
        if self.unicode:
            return s
        repl = {
            "€": "EUR ", "–": "-", "—": "-",
            "‘": "'", "’": "'", "“": '"', "”": '"',
            "→": "->", "≤": "<=", "≥": ">=", "±": "+/-",
            "×": "x", "•": "-", "²": "2", "³": "3",
            "…": "...", "º": "deg", "°": "deg",
        }
        for k, v in repl.items():
            s = s.replace(k, v)
        return s.encode("latin-1", "replace").decode("latin-1")

    def f(self, style="", size=11):
        self.set_font(self.base, style if self.unicode else style, size)

    # ----------------------------- page chrome ----------------------------- #
    def header(self):
        if not self._draw_header_footer:
            return
        self.set_fill_color(*GREEN)
        self.rect(0, 0, 6, self.h, style="F")  # left brand spine
        # small wordmark top-right
        self.set_xy(18, 9)
        self._wordmark(small=True)
        self.set_xy(-90, 11)
        self.f("", 8)
        self.set_text_color(*GREY)
        self.cell(72, 5, self.t(self.doc_sub), align="R")
        self.set_draw_color(*LINE)
        self.set_line_width(0.3)
        self.line(18, 18, self.w - 18, 18)
        self.set_y(24)

    def footer(self):
        if not self._draw_header_footer:
            return
        self.set_y(-15)
        self.set_draw_color(*LINE)
        self.set_line_width(0.3)
        self.line(18, self.get_y(), self.w - 18, self.get_y())
        self.set_y(-12)
        self.f("", 7.5)
        self.set_text_color(*GREY)
        self.cell(0, 5, self.t(f"E-Farm  -  {PROJECT_URL}"), align="L")
        self.set_y(-12)
        self.cell(0, 5, self.t(f"{self.doc_title}  -  {VERSION}  -  Page {self.page_no()}"),
                  align="R")

    # ------------------------- drawing primitives --------------------------- #
    def _wordmark(self, small=False, x=None, y=None, scale=1.0):
        """Draw a simple vector leaf+wordmark logo (no external image needed)."""
        if x is None:
            x = self.get_x()
        if y is None:
            y = self.get_y()
        r = (2.6 if small else 5.0) * scale
        cx, cy = x + r, y + r
        # leaf-circle mark
        self.set_fill_color(*GREEN)
        self.ellipse(x, y, 2 * r, 2 * r, style="F")
        # inner notch (white wedge) to suggest a leaf
        self.set_fill_color(*WHITE)
        self.ellipse(cx - r * 0.15, y + r * 0.35, r * 1.1, r * 0.55, style="F")
        # wordmark
        self.set_xy(x + 2 * r + (1.5 if small else 3), y - (0.2 if small else 0.5))
        self.f("B", 11 if small else 22)
        self.set_text_color(*GREEN_DARK)
        self.cell((30 if small else 60), (2 * r), self.t("E-Farm"),
                  align="L")

    def h1(self, text):
        if self.get_y() > self.h - 50:
            self.add_page()
        self.ln(2)
        self.f("B", 15)
        self.set_text_color(*GREEN_DARK)
        self.multi_cell(0, 7.5, self.t(text))
        self.set_draw_color(*GREEN)
        self.set_line_width(0.8)
        y = self.get_y() + 0.5
        self.line(18, y, 42, y)
        self.ln(3.5)

    def h2(self, text):
        if self.get_y() > self.h - 40:
            self.add_page()
        self.ln(1.5)
        self.f("B", 11.5)
        self.set_text_color(*GREEN)
        self.multi_cell(0, 6, self.t(text))
        self.ln(0.8)

    def body(self, text, size=10):
        self.f("", size)
        self.set_text_color(*INK)
        self.multi_cell(0, 5.2, self.t(text))
        self.ln(1.2)

    def bullet(self, text, size=10):
        self.f("", size)
        self.set_text_color(*INK)
        x = self.get_x()
        self.set_text_color(*GREEN)
        self.cell(5, 5.0, self.t("-"))
        self.set_text_color(*INK)
        self.multi_cell(0, 5.0, self.t(text))
        self.set_x(x)
        self.ln(0.4)

    def kv_table(self, rows, c0=58, label_head=None, val_head=None,
                 zebra=True):
        """Two-column spec/term table with wrapping right column."""
        avail = self.w - 36
        c1 = avail - c0
        if label_head:
            self.f("B", 9.5)
            self.set_fill_color(*GREEN)
            self.set_text_color(*WHITE)
            self.cell(c0, 7, self.t(" " + label_head), border=0, fill=True)
            self.cell(c1, 7, self.t(" " + val_head), border=0, fill=True,
                      new_x="LMARGIN", new_y="NEXT")
        i = 0
        for k, v in rows:
            self.f("B", 9)
            kx, ky = self.get_x(), self.get_y()
            # measure height needed for the value cell
            self.f("", 9)
            lines = self.multi_cell(c1, 5.0, self.t(v), dry_run=True,
                                    output="LINES")
            n = max(1, len(lines))
            rowh = max(7, n * 5.0 + 2)
            if self.get_y() + rowh > self.h - 20:
                self.add_page()
                kx, ky = self.get_x(), self.get_y()
            if zebra and i % 2 == 1:
                self.set_fill_color(*GREEN_LIGHT)
                self.rect(kx, ky, c0 + c1, rowh, style="F")
            self.set_draw_color(*LINE)
            self.set_line_width(0.2)
            self.set_xy(kx, ky)
            self.f("B", 9)
            self.set_text_color(*GREEN_DARK)
            self.multi_cell(c0, rowh, self.t(" " + k), border="B", align="L")
            self.set_xy(kx + c0, ky)
            self.f("", 9)
            self.set_text_color(*INK)
            # vertically center-ish single line vs wrap
            pad = (rowh - n * 5.0) / 2 if n * 5.0 < rowh else 1
            self.set_xy(kx + c0, ky + pad)
            self.multi_cell(c1, 5.0, self.t(" " + v), align="L")
            self.set_xy(kx + c0, ky)
            self.cell(c1, rowh, "", border="B")
            self.set_xy(kx, ky + rowh)
            i += 1
        self.ln(2)

    def callout(self, title, text):
        x = self.get_x()
        y = self.get_y()
        self.f("", 9.5)
        body_lines = self.multi_cell(self.w - 36 - 8, 4.8, self.t(text),
                                     dry_run=True, output="LINES")
        h = 9 + max(1, len(body_lines)) * 4.8 + 4
        if y + h > self.h - 20:
            self.add_page()
            y = self.get_y()
        self.set_fill_color(*GREEN_LIGHT)
        self.set_draw_color(*GREEN)
        self.rect(18, y, self.w - 36, h, style="F")
        self.set_fill_color(*GREEN)
        self.rect(18, y, 1.6, h, style="F")
        self.set_xy(22, y + 2.5)
        self.f("B", 10)
        self.set_text_color(*GREEN_DARK)
        self.cell(0, 5, self.t(title), new_x="LMARGIN", new_y="NEXT")
        self.set_x(22)
        self.f("", 9.5)
        self.set_text_color(*INK)
        self.multi_cell(self.w - 36 - 8, 4.8, self.t(text))
        self.set_y(y + h + 3)


# --------------------------------------------------------------------------- #
# Shared data
# --------------------------------------------------------------------------- #
REFERENCES = [
    ("Wang, Z., et al. (2024). Tomato ripeness and stem detection for robotic "
     "harvesting. Agriculture, 14(5), 751.", "doi:10.3390/agriculture14050751"),
    ("Xiao, F., et al. (2024). A review of fruit-picking robot vision and "
     "control. Multimedia Tools and Applications.", "doi:10.1007/s11042-023-16570-9"),
    ("Kang, H., et al. (2022). Visual perception and modelling for autonomous "
     "apple harvesting.", "arXiv:2205.00404"),
    ("Farhan, S. M., et al. (2024). Deep-learning detection and pose estimation "
     "for greenhouse harvesting. Sensors, 24(16), 5409.", "doi:10.3390/s24165409"),
    ("Rajendran, V., et al. (2024). Towards autonomous selective harvesting. "
     "Journal of Field Robotics.", "doi:10.1002/rob.22230"),
    ("Parsa, S., et al. (2024). Modular robotic system for soft-fruit "
     "harvesting. Journal of Field Robotics.", "doi:10.1002/rob.22229"),
    ("Lehnert, C., et al. (2017). Autonomous sweet-pepper harvesting in "
     "protected cropping systems.", "arXiv:1706.02023"),
    ("Li, Y., et al. (2024). A survey of robotic harvesting systems and "
     "enabling technologies.", "arXiv:2405.06959"),
]

COMPETITORS = [
    ("Octinion / Rubion (BE)", "Strawberry picking; table-top systems."),
    ("Agrobot (ES)", "Strawberry harvester with multi-arm gantry."),
    ("Root AI / Virgo (US)", "Greenhouse tomato/cucumber harvesting."),
    ("Tortuga AgTech (US)", "Strawberry/grape robotic harvest-as-a-service."),
    ("FFRobotics (IL)", "Multi-gripper orchard fruit harvester."),
    ("Four Growers (US)", "Greenhouse tomato harvesting robot."),
    ("Saga Robotics / Thorvald (NO)", "Modular agri-robot platform, UV + harvest."),
]


# --------------------------------------------------------------------------- #
# 1) WHITEPAPER
# --------------------------------------------------------------------------- #
def build_whitepaper(path):
    pdf = EFarmPDF("E-Farm Technical Overview & Vision", "Technical Whitepaper")

    # ---- Cover (no header/footer) ----
    pdf._draw_header_footer = False
    pdf.add_page()
    pdf.set_fill_color(*GREEN)
    pdf.rect(0, 0, pdf.w, 78, style="F")
    pdf.set_fill_color(*GREEN_DARK)
    pdf.rect(0, 74, pdf.w, 4, style="F")
    # mark on cover
    pdf.set_fill_color(*WHITE)
    pdf.ellipse(20, 22, 22, 22, style="F")
    pdf.set_fill_color(*GREEN)
    pdf.ellipse(24.5, 30, 13, 7, style="F")
    pdf.set_xy(48, 24)
    pdf.f("B", 30)
    pdf.set_text_color(*WHITE)
    pdf.cell(0, 12, pdf.t("E-Farm"), new_x="LMARGIN", new_y="NEXT")
    pdf.set_xy(48, 38)
    pdf.f("", 11)
    pdf.cell(0, 6, pdf.t("Autonomous Greenhouse Harvesting, Engineered Openly"))

    pdf.set_xy(18, 110)
    pdf.f("B", 26)
    pdf.set_text_color(*GREEN_DARK)
    pdf.multi_cell(0, 11, pdf.t("Technical Overview & Vision"))
    pdf.ln(2)
    pdf.set_x(18)
    pdf.f("", 13)
    pdf.set_text_color(*GREY)
    pdf.multi_cell(0, 7, pdf.t("An open-source robotics platform for multi-crop "
                               "greenhouse harvesting"))
    pdf.ln(8)
    pdf.set_x(18)
    pdf.f("B", 12)
    pdf.set_text_color(*GREEN)
    pdf.cell(0, 7, pdf.t(f"{YEAR}   -   {VERSION}"), new_x="LMARGIN", new_y="NEXT")

    pdf.set_xy(18, 230)
    pdf.set_draw_color(*LINE)
    pdf.line(18, 228, pdf.w - 18, 228)
    pdf.f("", 9)
    pdf.set_text_color(*GREY)
    pdf.multi_cell(0, 5, pdf.t(
        "Founded 2022 - Gebze, Bilisim Vadisi (Informatics Valley), Turkiye\n"
        f"Open-source monorepo: {PROJECT_URL}\n"
        "This document contains forward-looking targets, explicitly labelled. "
        "Figures cited are from the listed public sources."))
    pdf._draw_header_footer = True

    # ---- Body ----
    pdf.add_page()

    pdf.h1("1. Executive Summary")
    pdf.body(
        "Greenhouse horticulture across Europe and the Mediterranean is being "
        "squeezed by a structural shortage of skilled manual labour. Harvesting "
        "is the single most labour-intensive task in protected cropping, and the "
        "available workforce is shrinking and ageing. E-Farm is our answer: an "
        "autonomous harvesting robot that combines computer vision, LiDAR and "
        "RGB-D depth sensing, and a six-axis manipulator with an adaptive "
        "gripper to identify ripe produce and harvest it without damaging the "
        "plant.")
    pdf.body(
        "E-Farm was founded in 2022 at Bilisim Vadisi (Informatics Valley) in "
        "Gebze, Turkiye. We are a five-person team that has spent roughly three "
        "years in research and development, building on open-source hardware and "
        "publishing our work openly. We are honest about where we are: this is a "
        "credible, working engineering effort moving from prototype toward a "
        "pilot and a crowdfunding-backed first production batch - not a finished "
        "mass-market product. The figures we present that look ahead are marked "
        "as targets.")
    pdf.callout(
        "What E-Farm is",
        "Vision-guided ripeness detection + LiDAR/RGB-D localisation + a "
        "6-axis arm and adaptive gripper, coordinated by an open ROS2/MQTT "
        "software stack. Designed for multi-crop greenhouses, built on "
        "open-source foundations, and documented in a public monorepo.")

    pdf.h1("2. The Problem")
    pdf.body(
        "The agricultural labour base is contracting sharply. Across the "
        "European Union the farm workforce fell by roughly 3.5 million "
        "full-time-equivalent (FTE) workers between 2009 and 2024, and the "
        "sector is ageing fast - only about 11% of EU farmers are under 40. "
        "Protected horticulture is especially exposed, because harvesting "
        "cannot easily be mechanised with conventional field equipment: each "
        "fruit must be located, assessed for ripeness, and picked individually "
        "without bruising the produce or damaging the plant.")
    pdf.body("The greenhouse sector this addresses is large:")
    pdf.bullet("Turkiye: approximately 77,600 ha of greenhouse area.")
    pdf.bullet("Antalya region (Turkiye) alone: approximately 31,600 ha.")
    pdf.bullet("Spain: approximately 76,600 ha of greenhouse area.")
    pdf.bullet("Netherlands: approximately 10,260 ha of (high-intensity) "
               "glasshouse area.")
    pdf.body(
        "These are dense, high-value production environments where a reliable "
        "autonomous harvester directly addresses the labour gap - and where the "
        "structured, repeatable layout of a greenhouse makes robotic navigation "
        "and manipulation tractable.")

    pdf.h1("3. Technology")
    pdf.h2("3.1 Computer vision - ripeness detection")
    pdf.body(
        "Perception is built on a YOLOv8 object-detection model trained through "
        "Roboflow on a custom dataset of over 10,000 annotated images spanning "
        "five crops. On our project test set the model reaches 98% "
        "ripeness-detection accuracy. The model distinguishes ripe from unripe "
        "produce and localises each fruit in the image, providing the targets "
        "the manipulator acts on.")
    pdf.h2("3.2 Depth sensing and localisation")
    pdf.body(
        "RGB-D cameras and a LiDAR unit fuse colour, texture and metric depth so "
        "the robot can resolve a fruit's position in 3D. The localisation target "
        "is sub-centimetre accuracy at the gripper, which is what makes "
        "collision-free approach and a clean pick possible inside dense canopy.")
    pdf.h2("3.3 Manipulation - 6-axis arm and gripper")
    pdf.body(
        "The manipulator is a six-axis arm derived from the open-source PAROL6 "
        "design (licensed GPLv3), giving us a fully documented, repairable and "
        "modifiable platform rather than a closed black box. It carries an "
        "adaptive gripper that conforms to differently sized and shaped fruit and "
        "applies controlled force to avoid bruising.")
    pdf.h2("3.4 Power and electronics")
    pdf.body(
        "The robot runs on a LiFePO4 battery pack managed by an ESP32-based "
        "battery management system (BMS). LiFePO4 chemistry is chosen for its "
        "safety, long cycle life and stable behaviour in the warm, humid "
        "greenhouse environment.")
    pdf.h2("3.5 Software and fleet stack")
    pdf.body(
        "The control stack is built on ROS2 with MQTT for lightweight telemetry "
        "and fleet coordination, allowing multiple robots to be supervised from a "
        "single dashboard and enabling future fleet operation.")

    pdf.h1("4. System Architecture")
    pdf.body(
        "E-Farm follows a clear sense-decide-act pipeline. The perception module "
        "(vision + depth) detects and localises ripe fruit. A harvest finite-"
        "state machine (FSM) plans the sequence - approach, grasp, detach, place "
        "- and dispatches motion commands to the arm controller. Throughout, a "
        "telemetry layer streams status, health and yield data over MQTT to the "
        "operator dashboard and fleet manager.")
    pdf.body("The end-to-end flow:")
    pdf.bullet("Perception: YOLOv8 detection + RGB-D/LiDAR depth fusion -> "
               "3D fruit targets.")
    pdf.bullet("Harvest FSM: target selection, motion planning, grasp and "
               "detach logic, error recovery.")
    pdf.bullet("Arm: 6-axis PAROL6-based manipulator + adaptive gripper "
               "executes the pick.")
    pdf.bullet("Telemetry: MQTT status, yield counters and health metrics to "
               "the fleet dashboard.")
    pdf.body(
        "All of this is developed in the open. The full hardware designs, "
        "firmware and software live in our public monorepo at "
        f"{PROJECT_URL}, so backers, integrators and researchers can inspect, "
        "audit and build on the system.")

    pdf.h1("5. Open-Source Philosophy & Team")
    pdf.body(
        "E-Farm is built openly on purpose. Agricultural robotics has long been "
        "dominated by closed, single-crop systems sold at prices that put them "
        "out of reach of most growers, and that cannot be repaired or adapted "
        "by the people who use them. We take the opposite stance: by building on "
        "documented open-source foundations - the PAROL6 manipulator (GPLv3) and "
        "a NASA JPL Open Source Rover-derived chassis - and publishing our own "
        "hardware, firmware and software in a single public monorepo, we give "
        "growers, integrators and researchers a platform they can understand, "
        "trust, repair and extend.")
    pdf.body(
        "We believe this is also the fastest credible path to reliability. Open "
        "development invites scrutiny, reuse of mature components, and "
        "contributions from a community that is far larger than any single "
        "company's engineering team. It lowers the total cost of ownership for "
        "growers and avoids the vendor lock-in that has slowed adoption of "
        "agricultural robotics to date.")
    pdf.h2("5.1 Team and approach")
    pdf.body(
        "E-Farm was founded in 2022 at Bilisim Vadisi (Informatics Valley) in "
        "Gebze, Turkiye - one of the country's principal technology hubs. The "
        "core team of five spans computer vision, robotics and mechatronics, "
        "embedded systems and power electronics, and software/fleet "
        "infrastructure. Over roughly three years of R&D we have moved from "
        "individual subsystems to an integrated prototype: a trained perception "
        "model, a working manipulator and gripper, a LiFePO4 power system with a "
        "custom BMS, and a ROS2/MQTT software stack tying them together.")
    pdf.body(
        "Our working method is deliberately incremental and evidence-driven. We "
        "validate each subsystem against measurable targets - detection "
        "accuracy, localisation error, pick success - before integrating it, and "
        "we keep the whole system in the open so progress can be verified rather "
        "than merely claimed.")

    pdf.h1("6. Deployment & Economics")
    pdf.body(
        "E-Farm is designed for the structured environment of a commercial "
        "greenhouse: produce grown in rows on predictable supports, with level "
        "or gently uneven floors and controlled lighting. This structure is what "
        "makes autonomous harvesting tractable - navigation follows known rows, "
        "and the manipulator works within a bounded, repeatable geometry.")
    pdf.body("A typical deployment proceeds in stages:")
    pdf.bullet("Survey and mapping of the greenhouse rows and crop layout.")
    pdf.bullet("Per-crop perception tuning using the existing trained models as "
               "a base, refined on the grower's produce.")
    pdf.bullet("Supervised pilot operation alongside staff, building confidence "
               "and capturing edge cases.")
    pdf.bullet("Routine autonomous harvesting with remote monitoring via the "
               "MQTT fleet dashboard, and eventual multi-robot operation.")
    pdf.body(
        "The economic case rests on the labour shortage described in Section 2. "
        "Where skilled harvesting labour is scarce, expensive or seasonal, a "
        "robot that works long shifts, reports its yield in real time and scales "
        "as a fleet addresses both cost and availability. Concrete throughput "
        "and cost-per-kg figures depend on crop, layout and configuration, and "
        "will be reported transparently from pilot data rather than promised in "
        "advance.")

    pdf.h1("7. Market")
    pdf.body(
        "The agricultural-robots market is growing quickly. According to "
        "MarketsandMarkets (2025), the global agricultural-robots market is "
        "valued at about USD 17.73 billion in 2025 and is projected to reach "
        "USD 56.26 billion by 2030 - a compound annual growth rate (CAGR) of "
        "roughly 26%. Harvesting robotics is one of the fastest-growing "
        "segments within that market, driven directly by the labour shortage "
        "described above.")
    pdf.callout(
        "Market at a glance (MarketsandMarkets, 2025)",
        "2025: USD 17.73B  ->  2030: USD 56.26B   |   CAGR ~26%")

    pdf.h1("8. Competitive Context")
    pdf.body(
        "Robotic harvesting is an active field. The notable players each tend to "
        "focus on a single crop or geography:")
    rows = [(name, desc) for name, desc in COMPETITORS]
    pdf.kv_table(rows, c0=62, label_head="Company / Platform",
                 val_head="Focus")
    pdf.body(
        "E-Farm's positioning is distinct on three axes. First, geography and "
        "cost base: we are built in Turkiye, close to one of the world's largest "
        "greenhouse footprints, with a competitive engineering cost structure. "
        "Second, openness: the platform is open-source end-to-end, which lowers "
        "the barrier for integrators and researchers and avoids vendor lock-in. "
        "Third, scope: we target multi-crop greenhouse harvesting rather than a "
        "single fruit, using a general-purpose vision + 6-axis manipulation "
        "approach.")

    pdf.h1("9. Risks and Roadmap")
    pdf.callout(
        "Honest risk note",
        "E-Farm is a small team productising an R&D prototype. Real risks "
        "remain: field reliability and pick success rates in dense canopy, "
        "cycle-time and throughput economics versus manual labour, "
        "manufacturing and supply-chain execution for a first hardware batch, "
        "and regulatory/safety certification. Forward-looking dates and "
        "performance figures in this document are targets, not guarantees.")
    pdf.body("Roadmap (dates beyond the present are targets):")
    pdf.bullet("2025 - Pilot: field trials of the integrated prototype in "
               "working greenhouses. (target)")
    pdf.bullet("2026 - Crowdfunding campaign and first production batch. "
               "(current)")
    pdf.bullet("2027 - Fleet: multi-robot deployments coordinated through the "
               "ROS2/MQTT stack. (target)")

    pdf.h1("10. Selected References")
    pdf.f("", 9)
    for i, (cite, ident) in enumerate(REFERENCES, 1):
        pdf.set_text_color(*GREEN_DARK)
        pdf.f("B", 9)
        x = pdf.get_x()
        pdf.cell(7, 5, pdf.t(f"{i}."))
        pdf.set_text_color(*INK)
        pdf.f("", 9)
        pdf.multi_cell(0, 5, pdf.t(f"{cite}  {ident}"))
        pdf.set_x(x)
        pdf.ln(1.2)

    pdf.output(path)


# --------------------------------------------------------------------------- #
# 2) DATASHEET
# --------------------------------------------------------------------------- #
def build_datasheet(path):
    pdf = EFarmPDF("E-Farm Technical Datasheet", "Technical Datasheet")
    pdf.add_page()

    pdf.f("B", 20)
    pdf.set_text_color(*GREEN_DARK)
    pdf.cell(0, 9, pdf.t("Technical Datasheet"), new_x="LMARGIN", new_y="NEXT")
    pdf.f("", 11)
    pdf.set_text_color(*GREY)
    pdf.cell(0, 6, pdf.t("Autonomous Greenhouse Harvesting Robot  -  "
                         f"{VERSION}  -  {YEAR}"),
             new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.f("", 9)
    pdf.set_text_color(*INK)
    pdf.multi_cell(0, 5, pdf.t(
        "Specifications below describe the E-Farm platform. Values marked "
        "(target) or (illustrative) are design goals for the first production "
        "batch and may change; verified figures are from our project test set "
        "and selected components."))
    pdf.ln(2)

    pdf.h2("Perception & Vision")
    pdf.kv_table([
        ("Vision model", "YOLOv8 object detection (trained via Roboflow)"),
        ("Training data", "10,000+ annotated images across 5 crops"),
        ("Ripeness accuracy", "98% on project test set (verified, internal)"),
        ("Detected crops", "5 greenhouse crops (e.g. tomato, pepper, cucumber)"),
        ("Depth sensing", "RGB-D camera + LiDAR fusion; sub-cm localisation (target)"),
    ], label_head="Parameter", val_head="Specification")

    pdf.h2("Manipulation")
    pdf.kv_table([
        ("Manipulator", "6-axis arm, PAROL6-based (open-source, GPLv3)"),
        ("Repeatability", "+/- 0.1 mm class (illustrative, design class)"),
        ("Reach", "~440 mm (target)"),
        ("Payload", "~1 kg (target)"),
        ("End-effector", "Adaptive gripper, force-limited soft grasp"),
    ], label_head="Parameter", val_head="Specification")

    pdf.h2("Mobility & Chassis")
    pdf.kv_table([
        ("Chassis", "NASA JPL Open Source Rover (OSR)-derived (illustrative)"),
        ("Drive", "Multi-wheel rocker-style platform for uneven greenhouse floors"),
        ("Navigation", "Vision + LiDAR aided, structured-row greenhouse operation"),
    ], label_head="Parameter", val_head="Specification")

    pdf.h2("Power & Electronics")
    pdf.kv_table([
        ("Battery", "LiFePO4 pack (safe, long-cycle chemistry)"),
        ("BMS", "ESP32-based battery management system"),
        ("Runtime", "~8 h per charge (target)"),
    ], label_head="Parameter", val_head="Specification")

    pdf.h2("Software & Connectivity")
    pdf.kv_table([
        ("OS / middleware", "ROS2 Humble"),
        ("Telemetry / fleet", "MQTT messaging; multi-robot fleet dashboard"),
        ("Architecture", "Perception -> harvest FSM -> arm -> telemetry"),
        ("Connectivity", "Wi-Fi / Ethernet; MQTT broker uplink"),
        ("Source", f"Open-source monorepo: {PROJECT_URL}"),
    ], label_head="Parameter", val_head="Specification")

    pdf.h2("Physical (illustrative / target)")
    pdf.kv_table([
        ("Footprint", "~700 x 600 mm (illustrative)"),
        ("Height", "~1,300 mm with arm stowed (illustrative)"),
        ("Mass", "~45 kg (illustrative)"),
        ("Operating env.", "Protected greenhouse, 0-40 deg C, high humidity"),
    ], label_head="Parameter", val_head="Specification")

    pdf.ln(1)
    pdf.callout(
        "Note on figures",
        "Items labelled (target) or (illustrative) are pre-production design "
        "goals. The vision accuracy figure is measured on our internal project "
        "test set. PAROL6 is licensed GPLv3; E-Farm's own designs are published "
        "open-source in the project monorepo.")

    pdf.output(path)


# --------------------------------------------------------------------------- #
# 3) TERM SHEET
# --------------------------------------------------------------------------- #
def build_term_sheet(path):
    pdf = EFarmPDF("E-Farm Crowdfunding Term Sheet", "Pledge & Term Sheet")
    pdf.add_page()

    pdf.f("B", 20)
    pdf.set_text_color(*GREEN_DARK)
    pdf.cell(0, 9, pdf.t("Crowdfunding Pledge & Term Sheet"),
             new_x="LMARGIN", new_y="NEXT")
    pdf.f("", 11)
    pdf.set_text_color(*GREY)
    pdf.cell(0, 6, pdf.t(f"E-Farm campaign {YEAR}  -  {VERSION}"),
             new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.f("", 9)
    pdf.set_text_color(*INK)
    pdf.multi_cell(0, 5, pdf.t(
        "All amounts are in euro (EUR) and are illustrative campaign targets. "
        "Pledging supports the development and first production batch of an "
        "open-source greenhouse harvesting robot. Please read the campaign "
        "terms and risk disclosure below before pledging."))
    pdf.ln(2)

    pdf.h2("Pledge Tiers")
    tiers = [
        ("Supporter", "EUR 25", "-",
         "Backer credit, project updates, digital backer pack and access to the "
         "open-source release notes. A thank-you tier, not a hardware unit."),
        ("Early-Bird Pilot", "EUR 19,900", "Limited: 25",
         "One E-Farm robot at the earliest discounted price, priority pilot "
         "onboarding and direct engineering support. Limited to 25 units."),
        ("Core Robot", "EUR 23,900", "-",
         "One E-Farm harvesting robot (standard configuration), documentation "
         "and software access, standard support."),
        ("Deluxe Deployment", "EUR 31,900", "-",
         "Core Robot plus extended end-effector set, on-site setup assistance "
         "(target), extended warranty and priority support."),
        ("Commercial Fleet", "EUR 110,000", "-",
         "Multi-robot package with fleet dashboard, integration support and "
         "volume pricing for commercial greenhouse operators."),
        ("Founder's Circle", "EUR 149,000", "-",
         "Top-tier partnership: fleet package, named recognition, roadmap input "
         "and dedicated engineering liaison."),
    ]
    # Custom 3-col + wrap table for tiers
    avail = pdf.w - 36
    c_name, c_price, c_lim = 38, 26, 22
    c_inc = avail - c_name - c_price - c_lim
    pdf.f("B", 9)
    pdf.set_fill_color(*GREEN)
    pdf.set_text_color(*WHITE)
    pdf.cell(c_name, 7, pdf.t(" Tier"), fill=True)
    pdf.cell(c_price, 7, pdf.t(" Pledge"), fill=True)
    pdf.cell(c_lim, 7, pdf.t(" Limit"), fill=True)
    pdf.cell(c_inc, 7, pdf.t(" What's included"), fill=True,
             new_x="LMARGIN", new_y="NEXT")
    for i, (name, price, lim, inc) in enumerate(tiers):
        pdf.f("", 8.5)
        lines = pdf.multi_cell(c_inc, 4.6, pdf.t(inc), dry_run=True,
                               output="LINES")
        rowh = max(10, len(lines) * 4.6 + 3)
        if pdf.get_y() + rowh > pdf.h - 22:
            pdf.add_page()
        x0, y0 = pdf.get_x(), pdf.get_y()
        if i % 2 == 1:
            pdf.set_fill_color(*GREEN_LIGHT)
            pdf.rect(x0, y0, avail, rowh, style="F")
        pdf.set_draw_color(*LINE)
        pdf.line(x0, y0 + rowh, x0 + avail, y0 + rowh)
        pdf.set_xy(x0, y0 + 1.5)
        pdf.f("B", 9)
        pdf.set_text_color(*GREEN_DARK)
        pdf.multi_cell(c_name, 4.6, pdf.t(" " + name))
        pdf.set_xy(x0 + c_name, y0 + 1.5)
        pdf.f("B", 9)
        pdf.set_text_color(*INK)
        pdf.multi_cell(c_price, 4.6, pdf.t(" " + price))
        pdf.set_xy(x0 + c_name + c_price, y0 + 1.5)
        pdf.f("", 8.5)
        pdf.set_text_color(*GREY)
        pdf.multi_cell(c_lim, 4.6, pdf.t(" " + lim))
        pdf.set_xy(x0 + c_name + c_price + c_lim, y0 + 1.5)
        pdf.f("", 8.5)
        pdf.set_text_color(*INK)
        pdf.multi_cell(c_inc, 4.6, pdf.t(" " + inc), align="L")
        pdf.set_xy(x0, y0 + rowh)
    pdf.ln(3)

    pdf.h2("Campaign Terms")
    pdf.bullet("Delivery target windows: hardware tiers are targeted for "
               "fulfilment in 2026-2027, following the pilot phase. These are "
               "estimated target windows, not guaranteed dates.")
    pdf.bullet("Pricing: all amounts are illustrative campaign targets in EUR "
               "and may be adjusted before binding orders are confirmed.")
    pdf.bullet("Refund / cancellation: the Supporter tier is a non-refundable "
               "contribution. Hardware-tier pledges may be cancelled for a "
               "refund of the pledged amount before the order moves into "
               "production; once production of a backer's unit begins, refunds "
               "are limited to amounts not yet committed to manufacturing.")
    pdf.bullet("Manufacturing / risk disclosure: E-Farm is an early-stage "
               "hardware project. Schedules, specifications and prices may "
               "change due to engineering, supply-chain or certification "
               "factors. Backing a hardware tier carries the normal risks of "
               "early-stage hardware crowdfunding, including delay.")
    pdf.bullet("Open-source: the platform is developed openly; backers receive "
               "access to documentation and the public monorepo at "
               f"{PROJECT_URL}.")

    pdf.callout(
        "Please note",
        "This term sheet is a plain-language summary for prospective backers "
        "and is not a contract or an offer of securities. Final binding terms "
        "are those presented on the campaign checkout at the time of pledging.")

    pdf.output(path)


# --------------------------------------------------------------------------- #
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    targets = [
        ("efarm-whitepaper.pdf", build_whitepaper),
        ("efarm-datasheet.pdf", build_datasheet),
        ("efarm-term-sheet.pdf", build_term_sheet),
    ]
    for name, fn in targets:
        out = os.path.join(OUT_DIR, name)
        fn(out)
        size = os.path.getsize(out)
        print(f"  wrote {name:28s} {size:>8,} bytes")
    if not UNICODE_FONT:
        print("  [note] No Unicode TTF found; used core fonts with ASCII "
              "substitution.", file=sys.stderr)
    else:
        print(f"  [font] Unicode font: {UNICODE_FONT}")


if __name__ == "__main__":
    main()
