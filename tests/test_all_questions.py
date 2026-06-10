import sys
from pathlib import Path
import json
import re

# Add parent directory to sys.path to resolve internal modules correctly
sys.path.append(str(Path(__file__).parent / "app"))

from graph import graph

TEST_CASES = [
  {"id": 1, "type": "in_corpus", "question": "What notice period applies when Bluecrest or Priya Nambiar ends the employment agreement?", "expected_facts": ["60 days", "laptops", "badges", "source code"], "expected_source_files": ["02_employment_agreement_excerpt.md"]},
  {"id": 2, "type": "in_corpus", "question": "How long is the non-compete after leaving Bluecrest, and when does it apply?", "expected_facts": ["12 months", "competitor", "same city", "client list"], "expected_source_files": ["02_employment_agreement_excerpt.md"]},
  {"id": 3, "type": "in_corpus", "question": "What kinds of information are called out as confidential in the Bluecrest excerpt?", "expected_facts": ["pricing sheets", "product roadmaps", "customer names", "confidential"], "expected_source_files": ["02_employment_agreement_excerpt.md"]},
  {"id": 4, "type": "in_corpus", "question": "What is the civil suit number and who are the parties in the transport invoice dispute memo?", "expected_facts": ["CV-2024-8812", "Arvind Mehta", "Northfield Logistics", "invoices", "damaged"], "expected_source_files": ["01_matter_memo_arvind_v_northfield.md"]},
  {"id": 5, "type": "in_corpus", "question": "Under the memo, what limitation period applies to contract claims under the fictional Riverside Code?", "expected_facts": ["three years", "breach"], "expected_source_files": ["01_matter_memo_arvind_v_northfield.md"]},
  {"id": 6, "type": "in_corpus", "question": "When is the next hearing in Arvind Mehta v. Northfield, and what is scheduled?", "expected_facts": ["15 August 2025", "witness", "billing"], "expected_source_files": ["01_matter_memo_arvind_v_northfield.md"]},
  {"id": 7, "type": "in_corpus", "question": "How many clear days before the listed date must parties file written arguments under the hearing notice rules?", "expected_facts": ["seven", "clear days", "late filings"], "expected_source_files": ["03_hearing_notice_template.md"]},
  {"id": 8, "type": "in_corpus", "question": "What time is case CV-2024-8812 listed, and what is it for?", "expected_facts": ["11:00", "invoice", "set-off"], "expected_source_files": ["03_hearing_notice_template.md"]},
  {"id": 9, "type": "in_corpus", "question": "What happened to case CV-2023-4401 (Lakeview Society v. City Water Board), and what is the next date?", "expected_facts": ["adjourned", "22 September 2025", "water"], "expected_source_files": ["03_hearing_notice_template.md"]},
  {"id": 10, "type": "in_corpus", "question": "For commercial suits above five lakh fictional rupees, what does Section 14 say about mediation?", "expected_facts": ["mediation", "30 days", "waive"], "expected_source_files": ["04_statute_style_excerpt_fictional.md"]},
  {"id": 11, "type": "in_corpus", "question": "If a contract fixes no interest rate, what rate may be awarded on admitted dues under Section 22?", "expected_facts": ["9%", "simple interest", "demand"], "expected_source_files": ["04_statute_style_excerpt_fictional.md"]},
  {"id": 12, "type": "in_corpus", "question": "What settlement offer did Northfield make in the counsel notes, and what counter-instruction did the client give?", "expected_facts": ["70%", "85%", "counterclaim", "1 August 2025"], "expected_source_files": ["05_counsel_notes_settlement.md"]},
  {"id": 13, "type": "in_corpus", "question": "Are the settlement talks described in the counsel notes binding? What is the reminder?", "expected_facts": ["without prejudice", "term sheet"], "expected_source_files": ["05_counsel_notes_settlement.md"]},
  {"id": 14, "type": "in_corpus", "question": "Who is the lessor and lessee for Unit 4B at Harbor View Tower, and what is the monthly rent?", "expected_facts": ["Kiran Patel", "Harbor Bean", "45,000"], "expected_source_files": ["06_property_lease_clause.md"]},
  {"id": 15, "type": "in_corpus", "question": "What is the security deposit amount, and within how many days must it be refunded after handover?", "expected_facts": ["1,35,000", "45 days"], "expected_source_files": ["06_property_lease_clause.md"]},
  {"id": 16, "type": "in_corpus", "question": "Is subletting allowed for the Harbor View lease without extra steps?", "expected_facts": ["not allowed", "consent"], "expected_source_files": ["06_property_lease_clause.md"]},
  {"id": "O1", "type": "out_of_corpus", "question": "What is the population of Riverside city?", "expected_behavior": "refuse_or_not_found", "expected_source_files": []},
  {"id": "O2", "type": "out_of_corpus", "question": "What penalty applies if Priya breaches the non-compete?", "expected_behavior": "refuse_or_not_found", "expected_source_files": []},
  {"id": "O3", "type": "out_of_corpus", "question": "Who won case CV-2024-8812?", "expected_behavior": "refuse_or_not_found", "expected_source_files": []}
]

def check_fact(fact, answer):
    fact_clean = " ".join(fact.lower().split())
    answer_clean = " ".join(answer.lower().split())
    
    # Check for digit matching with/without commas
    if re.match(r'^[\d,%\.\-\s]+$', fact_clean):
        fact_digits = re.sub(r'[\s,]', '', fact_clean)
        answer_digits = re.sub(r'[\s,]', '', answer_clean)
        return (fact_clean in answer_clean) or (fact_digits in answer_digits)
    return fact_clean in answer_clean

if __name__ == "__main__":
    report_rows = []
    
    print(f"Starting evaluation of {len(TEST_CASES)} questions...\n")
    
    for tc in TEST_CASES:
        qid = tc["id"]
        qtype = tc["type"]
        question = tc["question"]
        print(f"Running Q{qid} ({qtype}): {question}")
        
        result = graph.invoke({"question": question})
        answer = result.get("answer", "")
        citations = [c.get("source_file") for c in result.get("citations", [])]
        
        # Fact check
        facts_status = []
        if qtype == "in_corpus":
            for fact in tc["expected_facts"]:
                passed = check_fact(fact, answer)
                facts_status.append((fact, "✅ Passed" if passed else "❌ Failed"))
        else:
            # For out of corpus, check if it refused
            refused = "could not find" in answer.lower() or "not present" in answer.lower() or "do not have" in answer.lower()
            facts_status.append(("refusal_message", "✅ Passed" if refused else "❌ Failed"))
            
        # Citations check
        citations_status = []
        for expected_file in tc["expected_source_files"]:
            passed = expected_file in citations
            citations_status.append((expected_file, "✅ Passed" if passed else "❌ Failed"))
            
        # Determine overall success
        all_facts_passed = all(status == "✅ Passed" for _, status in facts_status)
        all_citations_passed = all(status == "✅ Passed" for _, status in citations_status)
        overall_status = "✅ PASS" if (all_facts_passed and all_citations_passed) else "⚠️ WARNING"
        
        report_rows.append({
            "id": qid,
            "type": qtype,
            "question": question,
            "answer": answer,
            "citations": citations,
            "facts_status": facts_status,
            "citations_status": citations_status,
            "status": overall_status
        })
        
        plain_status = "PASS" if "PASS" in overall_status else "WARNING"
        print(f"  Status: {plain_status}\n")

    # Generate Markdown Report
    markdown_content = f"""# Legixo Legal RAG Evaluation Report

This report evaluates the compiled LangGraph state machine across **{len(TEST_CASES)} test questions** (16 in-corpus questions and 3 out-of-corpus questions).

---

## Executive Summary

| Total Questions | Passed | Warnings/Failures | Success Rate |
| :---: | :---: | :---: | :---: |
| {len(TEST_CASES)} | {sum(1 for r in report_rows if r["status"] == "✅ PASS")} | {sum(1 for r in report_rows if r["status"] != "✅ PASS")} | {(sum(1 for r in report_rows if r["status"] == "✅ PASS") / len(TEST_CASES)) * 100:.1f}% |

---

## Detailed Evaluation Table

| ID | Type | Question | Citations | Status |
| :---: | :---: | :--- | :--- | :---: |
"""
    for r in report_rows:
        citations_str = ", ".join(r["citations"]) if r["citations"] else "*None*"
        markdown_content += f"| {r['id']} | `{r['type']}` | {r['question']} | {citations_str} | **{r['status']}** |\n"
        
    markdown_content += "\n---\n\n## Question Details & Outputs\n\n"
    
    for r in report_rows:
        facts_details = "\n".join([f"* **{f}**: {s}" for f, s in r["facts_status"]])
        citations_details = "\n".join([f"* **{c}**: {s}" for c, s in r["citations_status"]]) if r["citations_status"] else "*No expected source files*"
        
        markdown_content += f"""### Question {r['id']} (`{r['type']}`)
**Question**: {r['question']}

**Answer**:
> {r['answer']}

**Citations**: {r['citations']}

**Facts Verification**:
{facts_details}

**Citations Verification**:
{citations_details}

---
"""

    # Write report to artifacts directory
    artifacts_dir = Path("C:/Users/HP/.gemini/antigravity-ide/brain/ec583160-2c65-4ba4-a868-fe41c9997f02")
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    report_file_path = artifacts_dir / "evaluation_report.md"
    
    with open(report_file_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
        
    print(f"Report written successfully to: {report_file_path}")
