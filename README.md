# Pentecost University IT Thesis & Academic Guardian Skill (`pentecost-it-thesis-guardian`)

[![Institution: Pentecost University](https://img.shields.io/badge/Institution-Pentecost%20University-blue.svg)](https://pentvars.edu.gh/)
[![Department: Information Technology](https://img.shields.io/badge/Department-Information%20Technology-green.svg)](https://pentvars.edu.gh/)
[![Faculty: FESC](https://img.shields.io/badge/Faculty-Engineering%2C%20Science%20%26%20Computing-blueviolet.svg)](https://pentvars.edu.gh/)
[![Degree: B.Sc. IT Final Year](https://img.shields.io/badge/Degree-B.Sc.%20Information%20Technology-orange.svg)](https://pentvars.edu.gh/)
[![Antigravity / Gemini Skill](https://img.shields.io/badge/Antigravity-Agent%20Skill%20v1.0-purple.svg)](https://github.com/s47user/pentecost-it-thesis-guardian)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

Universal, reusable Antigravity & Gemini AI agent skill designed for undergraduate final year projects (Level 400 B.Sc. Information Technology) at the **Department of Information Technology, Faculty of Engineering, Science and Computing, Pentecost University**, Sowutuom, Accra, Ghana.

This skill equips any AI coding or academic assistant with the departmental submission standards, strict word count limits, anti-slop academic directives, OpenXML layout protocols, and automated document verification tools required to produce defect-free project reports.

---

## 1. Core Capabilities & What This Skill Enforces

1. **Strict Departmental Word Count Limits**:
   - **Executive Summary / Abstract**: Strictly **200 – 250 words**, written in **One (1) single paragraph**.
   - **Introduction Section Summary**: Strictly **40 – 50 words**.
   - **Chapter Summary**: Strictly **80 – 100 words**.
   - **Chapter 1 (Introduction)**: Strictly **800 – 1,000 words**.
   - **Chapter 2 (Literature Review)**: **1,500 – 2,000 words**.
   - **Chapter 3 (Methodology)**: **2,500 – 3,000 words**.
   - **Chapter 4 (System Analysis & Design)**: **2,000 – 2,500 words**.
   - **Chapter 5 (Implementation & Evaluation)**: **2,000 – 2,500 words**.
2. **Page Geometry & Binding Margins**:
   - **Left Margin**: **35 mm to 40 mm** (mandatory binding allowance).
   - **Right Margin**: **20 mm to 25 mm**.
   - **Top Margin**: **30 mm to 35 mm**.
   - **Bottom Margin**: **25 mm to 30 mm**.
   - Times New Roman 12 pt, 1.5 line spacing, Justified text.
3. **Defensive Layout & OpenXML Tab Stops**:
   - Declaration signatures: Explicit tab stop at **4.2 inches**.
   - Abbreviations list: Explicit tab stop at **1.4 inches**.
   - Prevents proportional font misalignment caused by repeated space characters.
4. **Zero "AI Slop" Directives**:
   - Banning hollow filler and clichés (*"rich tapestry"*, *"beacon"*, *"delve into"*, *"not merely X, but Y"*).
   - Mandating affirmative, empirical technical claims backed by IEEE citations with authentic DOIs.
5. **Document Engineering & Defect Prevention**:
   - Eliminates the *Dynamic List-Offset Bug* by enforcing XML DOM sibling navigation over static paragraph indexing.

---

## 2. Quick-Start: How to Import Into Your Gemini / Antigravity Agent

Any student or collaborator can install and activate this skill in their AI development environment with a single command:

### Option A: Install as a Workspace Project Skill (Recommended)
Inside your project repository root:

```powershell
# PowerShell / Windows:
New-Item -ItemType Directory -Path ".agents\skills" -Force
git clone https://github.com/s47user/pentecost-it-thesis-guardian.git .agents\skills\pentecost-it-thesis-guardian
```

```bash
# Linux / macOS / Bash:
mkdir -p .agents/skills
git clone https://github.com/s47user/pentecost-it-thesis-guardian.git .agents/skills/pentecost-it-thesis-guardian
```

### Option B: Install Globally Across All Projects
To enable this skill for all workspaces on your machine:

```powershell
# PowerShell:
git clone https://github.com/s47user/pentecost-it-thesis-guardian.git "$HOME\.gemini\config\skills\pentecost-it-thesis-guardian"
```

```bash
# Linux / macOS:
git clone https://github.com/s47user/pentecost-it-thesis-guardian.git ~/.gemini/config/skills/pentecost-it-thesis-guardian
```

Once installed, Antigravity and Gemini automatically detect and index the skill.

---

## 3. Directory Layout & Bundled Resources

```text
pentecost-it-thesis-guardian/
├── SKILL.md                                  # Core agent instructions, triggers & runbook
├── README.md                                 # Skill documentation & import guide
├── LICENSE                                   # MIT open-source license
├── references/
│   ├── pentecost_it_thesis_guidelines.md     # Official 5-chapter thesis structure & word limits
│   ├── anti_slop_and_academic_standards.md   # Prohibited clichés, IEEE citation rules & writing standards
│   └── inspection_and_audit_protocols.md     # 5-Gate pre-flight checklist & tab-stop rules
├── scripts/
│   └── verify_academic_docx.py               # Automated Python audit script checking word counts & layout
└── examples/
    ├── executive_summary_template.md         # Gold-standard 208-word single-paragraph sample
    └── chapter_summary_template.md           # Gold-standard 92-word chapter summary sample
```

---

## 4. Automated Pre-Submission Quality Audit

This repository includes a standalone Python verification script to audit any generated Word thesis document (`.docx`) before submitting it to a lecturer or supervisor:

```powershell
python scripts/verify_academic_docx.py --file path/to/your_thesis_document.docx
```

### What the Audit Script Verifies:
* **Gate 1**: Detects unreplaced template placeholders (`student name`, `student id`).
* **Gate 2**: Verifies Declaration heading, signature lines, and date blocks.
* **Gate 3**: Confirms the Abbreviations section is cleanly isolated and detects if dynamic insertions leaked body paragraphs into the acronym table.
* **Gate 4**: Asserts that the Executive Summary is strictly between **200 and 250 words** and formatted as **One (1) single paragraph**.
* **Gate 5**: Asserts Chapter One subsections, Introduction Section Summary ($40 \le \text{words} \le 50$), Chapter Summary ($80 \le \text{words} \le 100$), and total Chapter One length ($800 \le \text{words} \le 1,000$).

---

## 5. Preliminary Pages Blueprint

1. **Title Page**
2. **Declaration** (with student signature and date blocks using 4.2" tab stop)
3. **Certification** (supervisor approval)
4. **Dedication**
5. **Acknowledgements**
6. **Table of Contents**
7. **List of Figures**
8. **List of Tables**
9. **Abbreviations** (1.4" tab stop)
10. **Executive Summary** (200–250 words, 1 paragraph, isolated on its own page)

---

## 6. License

Published under the **MIT License**. Free for all students and academic researchers.
