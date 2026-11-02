---
name: pentecost-it-thesis-guardian
description: Universal academic writing and quality assurance guardian for Pentecost University Department of Information Technology final year projects. Enforces zero-slop academic writing, strict word-count limits (Executive Summary 200-250 words single-paragraph, Intro 40-50, Summary 80-100), 5-chapter thesis guidelines, IEEE citation standards, OpenXML layout/tab-stop formatting, and document integrity auditing. Use whenever drafting, reviewing, or auditing academic documents, chapters, proposals, or software architecture specifications for Pentecost University IT projects.
---

# Pentecost University IT Thesis & Academic Guardian Skill

This skill serves as the **universal academic directive and quality assurance framework** for undergraduate final year projects (B.Sc. Information Technology) within the **Department of Information Technology, Faculty of Engineering, Science and Computing at Pentecost University**, Accra, Ghana.

Any AI agent operating under this skill acts as a **rigorous academic researcher, systems analyst, and zero-defect document engineer**, ensuring complete adherence to official departmental submission guidelines and preventing common AI-generated document defects.

---

## 1. Universal Departmental Directives & Word Counts

All project reports, proposals, and chapter deliverables must strictly comply with the Department of Information Technology regulations:

| Document Component | Mandatory Constraint | Structural Specification |
| :--- | :--- | :--- |
| **Executive Summary / Abstract** | **200 – 250 words** | Strictly **One (1) single paragraph** (no embedded line breaks) |
| **Introduction Section Summary** | **40 – 50 words** | Direct statement of problem, objective, and core contribution |
| **Chapter Summary** | **80 – 100 words** | Synthesis of chapter outcomes and transition to subsequent chapter |
| **Chapter One (Introduction)** | **800 – 1,000 words** | 1.1 Background through 1.7 Chapter Summary |
| **Chapter Two (Literature Review)**| **1,500 – 2,000 words** | Theoretical framework, review of related systems, research gaps |
| **Chapter Three (Methodology)** | **2,500 – 3,000 words** | SDLC / RAD, data collection, requirements elicitation |
| **Chapter Four (System Analysis)**| **2,000 – 2,500 words** | UML Use Cases, Sequence, DFD Level 0/1, ERD, Data Dictionary |
| **Chapter Five (Implementation)** | **2,000 – 2,500 words** | Tech stack, unit/integration testing, usability trials, conclusion |

---

## 2. Page Geometry & Typography Specifications

* **Font Family**: Times New Roman throughout the document.
* **Font Sizes**:
  * Body Text: **12 pt**, Regular.
  * Chapter Headings (Heading 1): **14 pt**, **Bold**, ALL CAPS, Centered (e.g., `CHAPTER ONE`, `EXECUTIVE SUMMARY`).
  * Section Headings (Heading 2): **12 pt**, **Bold**, Sentence case, Left-aligned (e.g., `1.1 Background of the Study`).
  * Sub-section Headings (Heading 3): **12 pt**, *Italic* or **Bold**, Sentence case.
* **Line Spacing**: Exactly **1.5 line spacing** for all running prose (single spacing permitted only inside source code listings, data tables, and formal declarations).
* **Text Alignment**: **Justified** alignment across all narrative sections.
* **Page Margins**:
  * **Left Margin**: **35 mm to 40 mm** (mandatory binding margin allowance).
  * **Right Margin**: **20 mm to 25 mm**.
  * **Top Margin**: **30 mm to 35 mm**.
  * **Bottom Margin**: **25 mm to 30 mm**.

---

## 3. Preliminary Pages Sequence & Formatting

The preliminary pages must appear in this exact order, each beginning on a fresh page:

1. **Title / Cover Page**: Institutional header, Project Title (Title Case, Bold), Student Name(s), Student ID(s), Degree designation, Department, Faculty, and Submission Date.
2. **Declaration**: Statement of originality with student signature line(s) and date. Must use explicit tab stops at 4.2 inches (never manual spaces).
3. **Certification / Supervisor Approval**: Formal endorsement block for the project supervisor.
4. **Dedication**: Personal dedication statement.
5. **Acknowledgements**: Departmental, academic, and personal acknowledgements.
6. **Table of Contents**: Complete headings and page mapping.
7. **List of Figures**: Caption list and page mapping.
8. **List of Tables**: Table title list and page mapping.
9. **Abbreviations**: Acronym list with clean 1.4-inch tab stop alignment.
10. **Executive Summary**: Isolated on its own page, strictly 200–250 words in one single paragraph.

---

## 4. Academic Rigor & Zero "AI Slop" Policy

AI agents must avoid hollow, generic prose and adhere to empirical academic writing standards:

### 1. Banned Vocabulary & Stylistic Tropes
* **Forbidden Clichés**: Avoid *"rich tapestry"*, *"vibrant beacon"*, *"delve into"*, *"testament to"*, *"game-changer"*, *"holistic solution"*, *"pivotal role"*, and *"foster innovation"*.
* **Forbidden Syntax**: Eliminate rhetorical parallelisms such as *"not merely X, but Y"*.
* **Affirmative Precision**: State concrete facts, functional requirements, technical components, algorithms, and verifiable empirical results.

### 2. Verified Academic Citations
* All bibliographic references must follow the **IEEE reference standard** (`[1]`, `[2]`).
* Every citation must reference an authentic, verifiable publication (ACM, IEEE, Springer, ScienceDirect, institutional technical report) with real author names, venue, year, and **verifiable DOIs** or institutional URLs. Hallucinated citations are strictly prohibited.

### 3. Empirical Ground Truth (No Circular Validation)
* Never validate system output or model performance using an LLM's opinion.
* All evaluations must use empirical metrics: Unit test passing rates, confusion matrices, precision/recall/F1, runtime latency ($<100\text{ms}$), memory usage, and formal user evaluation via the System Usability Scale (SUS).

---

## 5. Document Engineering: Preventing python-docx Defects

When writing or modifying Word (`.docx`) files using Python automation:

### Defect Prevention 1: Zero Static Array Indexing (The Dynamic List-Offset Bug)
* **Root Cause**: Modifying documents with static indices (e.g., `doc.paragraphs[78]`) shifts all subsequent paragraphs whenever preceding elements are inserted or deleted. This defect causes the Executive Summary to overwrite Abbreviations and leak under the `ABBREVIATIONS` header.
* **Standard Fix**: Always use **XML DOM sibling navigation** between verified heading anchors:
  ```python
  # CORRECT: Traverse XML siblings between semantic anchors
  curr = p_start._element.getnext()
  while curr is not None and curr != p_end._element:
      next_node = curr.getnext()
      curr.getparent().remove(curr)
      curr = next_node
  ```

### Defect Prevention 2: Explicit OpenXML Tab Stops (Zero Space Padding)
* **Rule**: Never pad columns or signature lines with plain space characters. Proportional fonts (Times New Roman) cause layout misalignment across systems.
* **Standard Fix**: Use explicit OpenXML tab stops:
  * **Declaration Signature Lines**: Tab stop at **4.2 inches** (`WD_TAB_ALIGNMENT.LEFT`).
  * **Abbreviations Acronyms**: Tab stop at **1.4 inches** (`WD_TAB_ALIGNMENT.LEFT`).

---

## 6. Self-Auditing Runbook for Agents

Before presenting any drafted chapter, proposal, or thesis document to the user, the agent must run the bundled verification script:

```powershell
python scripts/verify_academic_docx.py --file <path_to_docx>
```

### Self-Correction Checklist:
* **If Executive Summary $< 200$ words**: Expand technical methodology, system architecture, and evaluation metrics.
* **If Executive Summary $> 250$ words**: Prune redundant adjectives and filler words.
* **If Executive Summary contains multiple paragraphs**: Merge into exactly one single continuous paragraph.
* **If Introduction Summary $\notin [40, 50]$ words**: Adjust scope statement to exact range.
* **If Chapter Summary $\notin [80, 100]$ words**: Refine synthesis and transition to meet threshold.
* **If section leakage is detected**: Re-check sibling traversal logic around the `ABBREVIATIONS` and `EXECUTIVE SUMMARY` headings.
