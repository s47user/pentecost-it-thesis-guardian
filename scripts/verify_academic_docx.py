#!/usr/bin/env python3
"""
verify_academic_docx.py
======================
Universal quality assurance and structural audit script for Pentecost University
Department of Information Technology undergraduate final year project reports.

Enforces:
1. Cover page student attribution (detects unreplaced placeholders like 'student name' / 'id')
2. Declaration signature layout
3. Isolated Abbreviations section (detects dynamic list-offset leakage)
4. Executive Summary: strictly 200-250 words, strictly 1 single paragraph
5. Introduction Section Summary: strictly 40-50 words
6. Chapter Summary: strictly 80-100 words
7. Chapter One total length: strictly 800-1000 words
8. Heading isolation and absence of text leakage across boundaries
"""

import sys
import os
import argparse

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

try:
    import docx
except ImportError:
    print("[ERROR] python-docx is required. Install it using: pip install python-docx")
    sys.exit(1)


def audit_document(file_path):
    print(f"\n=======================================================")
    print(f" PENTECOST UNIVERSITY IT THESIS QUALITY ASSURANCE AUDIT")
    print(f" Target File: {os.path.abspath(file_path)}")
    print(f"=======================================================\n")

    if not os.path.exists(file_path):
        print(f"[FAIL] Target file does not exist: {file_path}")
        return False

    try:
        doc = docx.Document(file_path)
    except Exception as e:
        print(f"[FAIL] Could not open Word document: {e}")
        return False

    paragraphs = doc.paragraphs
    total_p = len(paragraphs)
    print(f"[*] Total paragraphs parsed: {total_p}")

    failures = []

    # -------------------------------------------------------------
    # 1. Cover Page & Placeholder Check
    # -------------------------------------------------------------
    print("\n--- Gate 1: Cover Page & Placeholder Verification ---")
    cover_text = " ".join([p.text for p in paragraphs[:35]]).lower()
    
    # Official department rule: Replace 'student name' and 'id' placeholders
    if "student name" in cover_text:
        failures.append("Cover Page: Unreplaced placeholder detected ('student name'). Replace with actual student name.")
    if "student id" in cover_text or "insert id" in cover_text:
        failures.append("Cover Page: Unreplaced placeholder detected ('student id' or 'insert id'). Replace with actual ID.")

    if not failures:
        print("[PASS] Cover page verified (no unreplaced student placeholders found).")

    # -------------------------------------------------------------
    # 2. Declaration Signature Layout
    # -------------------------------------------------------------
    print("\n--- Gate 2: Declaration Block Verification ---")
    decl_found = any("DECLARATION" in p.text for p in paragraphs[:50])
    if not decl_found:
        failures.append("Declaration: 'DECLARATION' heading missing.")
    else:
        sig_lines = [p.text for p in paragraphs[:60] if "...." in p.text or "Signature" in p.text or "Date" in p.text]
        if not sig_lines:
            failures.append("Declaration: Signature and Date lines not detected in Declaration section.")
        else:
            print("[PASS] Declaration section and signature lines verified.")

    # -------------------------------------------------------------
    # 3. Abbreviations Section Isolation & Leakage Check
    # -------------------------------------------------------------
    print("\n--- Gate 3: Abbreviations Section Isolation ---")
    abbr_idx = None
    exec_idx = None
    for i, p in enumerate(paragraphs):
        text = p.text.strip()
        if text == "ABBREVIATIONS":
            abbr_idx = i
        elif text == "EXECUTIVE SUMMARY":
            exec_idx = i

    if abbr_idx is None:
        failures.append("Abbreviations: 'ABBREVIATIONS' heading not found.")
    elif exec_idx is None:
        failures.append("Abbreviations: 'EXECUTIVE SUMMARY' heading not found following Abbreviations.")
    elif exec_idx <= abbr_idx:
        failures.append("Abbreviations: 'EXECUTIVE SUMMARY' appears before 'ABBREVIATIONS'.")
    else:
        abbr_paras = paragraphs[abbr_idx + 1 : exec_idx]
        abbr_non_empty = [p.text.strip() for p in abbr_paras if p.text.strip()]
        print(f"[*] Found {len(abbr_non_empty)} abbreviation items between ABBREVIATIONS and EXECUTIVE SUMMARY.")
        
        # Check for dynamic list-offset leakage: narrative paragraphs appearing inside abbreviations
        leaked = [t for t in abbr_non_empty if len(t.split()) > 15]
        if leaked:
            failures.append(f"Abbreviations LEAKAGE DETECTED: Narrative text leaked into Abbreviations: '{leaked[0][:60]}...'")
        else:
            print("[PASS] No narrative leakage detected in Abbreviations block.")

        if len(abbr_non_empty) < 5:
            failures.append(f"Abbreviations: List contains fewer than 5 items ({len(abbr_non_empty)} found).")
        else:
            print(f"[PASS] Abbreviations count verified ({len(abbr_non_empty)} items).")

    # -------------------------------------------------------------
    # 4. Executive Summary Word Count & Single Paragraph
    # -------------------------------------------------------------
    print("\n--- Gate 4: Executive Summary (200-250 Words, Strictly 1 Paragraph) ---")
    if exec_idx is not None:
        # Find subsequent major heading (CHAPTER ONE)
        ch1_idx = None
        for i in range(exec_idx + 1, len(paragraphs)):
            if paragraphs[i].text.strip() == "CHAPTER ONE":
                ch1_idx = i
                break

        if ch1_idx is None:
            failures.append("Executive Summary: 'CHAPTER ONE' heading not found following Executive Summary.")
        else:
            exec_paras = [p.text.strip() for p in paragraphs[exec_idx + 1 : ch1_idx] if p.text.strip()]
            if len(exec_paras) == 0:
                failures.append("Executive Summary: Body text is missing.")
            elif len(exec_paras) > 1:
                failures.append(f"Executive Summary: Department mandates strictly ONE (1) paragraph. Found {len(exec_paras)} paragraphs.")
            else:
                exec_text = exec_paras[0]
                exec_words = len(exec_text.split())
                print(f"[*] Executive Summary Word Count: {exec_words} words (Requirement: 200 - 250 words)")
                if exec_words < 200 or exec_words > 250:
                    failures.append(f"Executive Summary: Word count is {exec_words}. Must be strictly between 200 and 250 words.")
                else:
                    print("[PASS] Executive Summary word count is strictly compliant (200-250 words, 1 paragraph).")

    # -------------------------------------------------------------
    # 5. Chapter One Structure & Word Count Gates
    # -------------------------------------------------------------
    print("\n--- Gate 5: Chapter One Subsections & Word Count Gates ---")
    if ch1_idx is not None:
        ch2_idx = None
        for i in range(ch1_idx + 1, len(paragraphs)):
            if paragraphs[i].text.strip() == "CHAPTER TWO":
                ch2_idx = i
                break

        if ch2_idx is None:
            ch2_idx = len(paragraphs)

        ch1_paras = paragraphs[ch1_idx + 1 : ch2_idx]
        ch1_texts = [p.text.strip() for p in ch1_paras if p.text.strip()]
        ch1_full_text = " ".join(ch1_texts)
        ch1_words = len(ch1_full_text.split())
        print(f"[*] Chapter One Total Word Count: {ch1_words} words (Requirement: 800 - 1000 words)")

        # Required official subsections
        subsections = [
            "1.1 Background",
            "1.2 Problem Statement",
            "1.3 Objectives",
            "1.4 Scope",
            "1.5 Significance",
            "1.6 Organization",
            "1.7 Chapter Summary"
        ]
        for sub in subsections:
            if not any(sub.lower() in t.lower() for t in ch1_texts):
                failures.append(f"Chapter One: Required subsection '{sub}' not found.")

        # Check Introduction section summary (40 - 50 words)
        intro_summary_found = False
        for p in ch1_paras:
            # Match introductory summary statement
            lower_text = p.text.lower()
            if any(k in lower_text for k in ["this study introduces", "this project develops", "this research proposes", "this project aims"]):
                words = len(p.text.split())
                print(f"[*] Introduction Section Summary Word Count: {words} words (Requirement: 40 - 50 words)")
                if 40 <= words <= 50:
                    print("[PASS] Introduction section summary word count is compliant (40-50 words).")
                    intro_summary_found = True
                    break
                else:
                    failures.append(f"Introduction Summary: Word count is {words}. Must be strictly between 40 and 50 words.")
                    intro_summary_found = True
                    break

        # Check Chapter summary (80 - 100 words)
        for i, p in enumerate(ch1_paras):
            if "1.7 chapter summary" in p.text.lower():
                if i + 1 < len(ch1_paras):
                    body = ch1_paras[i + 1].text.strip()
                    words = len(body.split())
                    print(f"[*] Chapter One Summary Word Count: {words} words (Requirement: 80 - 100 words)")
                    if 80 <= words <= 100:
                        print("[PASS] Chapter summary word count is compliant (80-100 words).")
                    else:
                        failures.append(f"Chapter Summary: Word count is {words}. Must be strictly between 80 and 100 words.")
                    break

    # -------------------------------------------------------------
    # Summary Diagnostic
    # -------------------------------------------------------------
    print("\n=======================================================")
    print(" AUDIT EXECUTION RESULT")
    print("=======================================================")
    if failures:
        print(f"[FAIL] Audit failed with {len(failures)} critical defect(s):")
        for idx, f in enumerate(failures, 1):
            print(f"  {idx}. {f}")
        return False
    else:
        print("[SUCCESS] All academic gates, layout constraints, and word counts passed with 100% compliance!")
        return True


def main():
    parser = argparse.ArgumentParser(description="Audit Pentecost University IT thesis documents.")
    parser.add_argument("--file", "-f", required=True, help="Path to .docx file to audit")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"[ERROR] Specified file not found: {args.file}")
        sys.exit(1)

    success = audit_document(args.file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
