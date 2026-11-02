# Quality Assurance & Word Document Inspection Protocol

This document establishes the mandatory quality gates and defect prevention methods required for any automated script, document generator, or AI assistant producing or modifying Word (`.docx`) thesis deliverables.

---

## 1. Root Cause Analysis: Preventing Common Document Generation Defects

When using Python libraries (such as `python-docx`) to generate or populate Word templates, automated pipelines often introduce critical structural bugs:

### Defect 1: The Dynamic List-Offset Bug
* **Mechanism**: Python scripts reference paragraph arrays using hardcoded indices (e.g., `doc.paragraphs[78]`) after previously adding or deleting paragraphs (e.g., populating an abbreviations list).
* **Impact**: Inserting items earlier in the document shifts the indices of all downstream document blocks. Code intended to populate the Executive Summary and Chapter One writes into shifted abbreviation slots, overwriting headings and leaking body text directly beneath the `ABBREVIATIONS` header.
* **Standard Resolution**: Never use static array indexing. Always use **DOM sibling navigation** relative to verified semantic headings.

### Defect 2: Space-Padding Misalignment
* **Mechanism**: Developers attempt to align columns (such as signature lines and abbreviation acronyms) using multiple space characters (`"STUDENT NAME          Date: ..."`).
* **Impact**: Proportional fonts (such as Times New Roman) assign varying widths to characters across platforms and printers, producing ragged, uneven columns.
* **Standard Resolution**: Align multi-column layouts strictly with **OpenXML tab stops** set at precise measurement points (`1.4 inches` and `4.2 inches`).

---

## 2. The 5 Pre-Flight Verification Gates

Before presenting any `.docx` report or chapter to a supervisor or evaluation panel, verify that the document satisfies all five gates:

### Gate 1: Strict DOM Sibling Navigation (Zero Static Indexing)
* **Standard Implementation (python-docx)**:
  ```python
  # Locate verified semantic anchors
  p_start = find_heading(doc, "ABBREVIATIONS")
  p_end = find_heading(doc, "EXECUTIVE SUMMARY")
  
  # Traverse XML DOM siblings directly
  curr = p_start._element.getnext()
  while curr is not None and curr != p_end._element:
      next_node = curr.getnext()
      curr.getparent().remove(curr)
      curr = next_node
  ```
* All insertions must use `.insert_paragraph_before()` tied to an existing validated heading or bookmark element.

### Gate 2: Heading Boundary & Section Isolation
Every primary section must exist under an independent, verified `Heading 1` boundary with `pageBreakBefore` enabled:
1. `TITLE PAGE`
2. `DECLARATION` [Heading 1]
3. `CERTIFICATION` [Heading 1]
4. `DEDICATION` [Heading 1]
5. `ACKNOWLEDGEMENT` [Heading 1]
6. `TABLE OF CONTENT` [Heading 1]
7. `LIST OF FIGURES` [Heading 1]
8. `LIST OF TABLES` [Heading 1]
9. `ABBREVIATIONS` [Heading 1]
10. `EXECUTIVE SUMMARY` [Heading 1] (isolated on its own page)
11. `CHAPTER ONE` [Heading 1] (isolated on its own page)
12. `CHAPTER TWO` through `CHAPTER FIVE`
13. `REFERENCE` [Heading 1]
14. `APPENDIX` [Heading 1]

**Zero Leakage Rule**: No narrative text belonging to one section may ever appear between the headings of another section.

### Gate 3: Explicit OpenXML Tab Stops
* Never use manual spaces for column indentation or alignment.
* **Declaration Signature Block**: Tab stop at **4.2 inches** (`WD_TAB_ALIGNMENT.LEFT`).
* **Abbreviations Acronym List**: Tab stop at **1.4 inches** (`WD_TAB_ALIGNMENT.LEFT`).

### Gate 4: Departmental Word Count Enforcement
* **Executive Summary**: Strictly **200 – 250 words**, strictly in **One (1) single paragraph** (no embedded line breaks or carriage returns).
* **Introduction Section Summary**: Strictly **40 – 50 words**.
* **Chapter Summary**: Strictly **80 – 100 words**.
* **Chapter One Total**: Strictly **800 – 1,000 words**.

### Gate 5: Execution of Automated Audit Script
* Run the verification test suite before submission:
  ```powershell
  python scripts/verify_academic_docx.py --file <path_to_docx>
  ```
* If any assertion fails, the assistant must refuse to report the deliverable as complete until the underlying fault is resolved.
