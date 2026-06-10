# Legixo Legal RAG Evaluation Report

This report evaluates the compiled LangGraph state machine across **19 test questions** (16 in-corpus questions and 3 out-of-corpus questions).

---

## Executive Summary

| Total Questions | Passed | Warnings/Failures | Success Rate |
| :---: | :---: | :---: | :---: |
| 19 | 17 | 2 | 89.5% |

---

## Detailed Evaluation Table

| ID | Type | Question | Citations | Status |
| :---: | :---: | :--- | :--- | :---: |
| 1 | `in_corpus` | What notice period applies when Bluecrest or Priya Nambiar ends the employment agreement? | 02_employment_agreement_excerpt.md, 02_employment_agreement_excerpt.md, 01_matter_memo_arvind_v_northfield.md, 03_hearing_notice_template.md, 04_statute_style_excerpt_fictional.md | **✅ PASS** |
| 2 | `in_corpus` | How long is the non-compete after leaving Bluecrest, and when does it apply? | 02_employment_agreement_excerpt.md, 02_employment_agreement_excerpt.md, 01_matter_memo_arvind_v_northfield.md, 03_hearing_notice_template.md, 04_statute_style_excerpt_fictional.md | **✅ PASS** |
| 3 | `in_corpus` | What kinds of information are called out as confidential in the Bluecrest excerpt? | 02_employment_agreement_excerpt.md, 02_employment_agreement_excerpt.md, 03_hearing_notice_template.md, 06_property_lease_clause.md, 01_matter_memo_arvind_v_northfield.md | **✅ PASS** |
| 4 | `in_corpus` | What is the civil suit number and who are the parties in the transport invoice dispute memo? | 01_matter_memo_arvind_v_northfield.md, 05_counsel_notes_settlement.md, 01_matter_memo_arvind_v_northfield.md, 03_hearing_notice_template.md, 04_statute_style_excerpt_fictional.md | **⚠️ WARNING** |
| 5 | `in_corpus` | Under the memo, what limitation period applies to contract claims under the fictional Riverside Code? | 01_matter_memo_arvind_v_northfield.md, 04_statute_style_excerpt_fictional.md, 05_counsel_notes_settlement.md, 02_employment_agreement_excerpt.md, 03_hearing_notice_template.md | **✅ PASS** |
| 6 | `in_corpus` | When is the next hearing in Arvind Mehta v. Northfield, and what is scheduled? | 03_hearing_notice_template.md, 05_counsel_notes_settlement.md, 01_matter_memo_arvind_v_northfield.md, 03_hearing_notice_template.md, 01_matter_memo_arvind_v_northfield.md | **✅ PASS** |
| 7 | `in_corpus` | How many clear days before the listed date must parties file written arguments under the hearing notice rules? | 03_hearing_notice_template.md, 01_matter_memo_arvind_v_northfield.md, 04_statute_style_excerpt_fictional.md, 03_hearing_notice_template.md, 05_counsel_notes_settlement.md | **⚠️ WARNING** |
| 8 | `in_corpus` | What time is case CV-2024-8812 listed, and what is it for? | 03_hearing_notice_template.md, 03_hearing_notice_template.md, 01_matter_memo_arvind_v_northfield.md, 01_matter_memo_arvind_v_northfield.md, 04_statute_style_excerpt_fictional.md | **✅ PASS** |
| 9 | `in_corpus` | What happened to case CV-2023-4401 (Lakeview Society v. City Water Board), and what is the next date? | 03_hearing_notice_template.md, 01_matter_memo_arvind_v_northfield.md, 01_matter_memo_arvind_v_northfield.md, 05_counsel_notes_settlement.md, 03_hearing_notice_template.md | **✅ PASS** |
| 10 | `in_corpus` | For commercial suits above five lakh fictional rupees, what does Section 14 say about mediation? | 04_statute_style_excerpt_fictional.md, 05_counsel_notes_settlement.md, 03_hearing_notice_template.md, 01_matter_memo_arvind_v_northfield.md, 01_matter_memo_arvind_v_northfield.md | **✅ PASS** |
| 11 | `in_corpus` | If a contract fixes no interest rate, what rate may be awarded on admitted dues under Section 22? | 04_statute_style_excerpt_fictional.md, 05_counsel_notes_settlement.md, 04_statute_style_excerpt_fictional.md, 03_hearing_notice_template.md, 01_matter_memo_arvind_v_northfield.md | **✅ PASS** |
| 12 | `in_corpus` | What settlement offer did Northfield make in the counsel notes, and what counter-instruction did the client give? | 05_counsel_notes_settlement.md, 01_matter_memo_arvind_v_northfield.md, 03_hearing_notice_template.md, 04_statute_style_excerpt_fictional.md, 03_hearing_notice_template.md | **✅ PASS** |
| 13 | `in_corpus` | Are the settlement talks described in the counsel notes binding? What is the reminder? | 05_counsel_notes_settlement.md, 03_hearing_notice_template.md, 04_statute_style_excerpt_fictional.md, 01_matter_memo_arvind_v_northfield.md, 01_matter_memo_arvind_v_northfield.md | **✅ PASS** |
| 14 | `in_corpus` | Who is the lessor and lessee for Unit 4B at Harbor View Tower, and what is the monthly rent? | 06_property_lease_clause.md, 03_hearing_notice_template.md, 01_matter_memo_arvind_v_northfield.md, 02_employment_agreement_excerpt.md, 04_statute_style_excerpt_fictional.md | **✅ PASS** |
| 15 | `in_corpus` | What is the security deposit amount, and within how many days must it be refunded after handover? | 06_property_lease_clause.md, 04_statute_style_excerpt_fictional.md, 01_matter_memo_arvind_v_northfield.md, 05_counsel_notes_settlement.md, 02_employment_agreement_excerpt.md | **✅ PASS** |
| 16 | `in_corpus` | Is subletting allowed for the Harbor View lease without extra steps? | 06_property_lease_clause.md, 03_hearing_notice_template.md, 04_statute_style_excerpt_fictional.md, 05_counsel_notes_settlement.md, 01_matter_memo_arvind_v_northfield.md | **✅ PASS** |
| O1 | `out_of_corpus` | What is the population of Riverside city? | *None* | **✅ PASS** |
| O2 | `out_of_corpus` | What penalty applies if Priya breaches the non-compete? | 02_employment_agreement_excerpt.md, 04_statute_style_excerpt_fictional.md, 02_employment_agreement_excerpt.md, 05_counsel_notes_settlement.md, 01_matter_memo_arvind_v_northfield.md | **✅ PASS** |
| O3 | `out_of_corpus` | Who won case CV-2024-8812? | 03_hearing_notice_template.md, 01_matter_memo_arvind_v_northfield.md, 05_counsel_notes_settlement.md, 01_matter_memo_arvind_v_northfield.md, 03_hearing_notice_template.md | **✅ PASS** |

---

## Question Details & Outputs

### Question 1 (`in_corpus`)
**Question**: What notice period applies when Bluecrest or Priya Nambiar ends the employment agreement?

**Answer**:
> The notice period is 60 days, during which the employee must hand over all laptops, badges, and source code access.

**Citations**: ['02_employment_agreement_excerpt.md', '02_employment_agreement_excerpt.md', '01_matter_memo_arvind_v_northfield.md', '03_hearing_notice_template.md', '04_statute_style_excerpt_fictional.md']

**Facts Verification**:
* **60 days**: ✅ Passed
* **laptops**: ✅ Passed
* **badges**: ✅ Passed
* **source code**: ✅ Passed

**Citations Verification**:
* **02_employment_agreement_excerpt.md**: ✅ Passed

---
### Question 2 (`in_corpus`)
**Question**: How long is the non-compete after leaving Bluecrest, and when does it apply?

**Answer**:
> The non-compete lasts for 12 months after leaving Bluecrest and applies if the new role is with a direct competitor in the same city where Bluecrest has an office, and uses the same client list supplied by Bluecrest.

**Citations**: ['02_employment_agreement_excerpt.md', '02_employment_agreement_excerpt.md', '01_matter_memo_arvind_v_northfield.md', '03_hearing_notice_template.md', '04_statute_style_excerpt_fictional.md']

**Facts Verification**:
* **12 months**: ✅ Passed
* **competitor**: ✅ Passed
* **same city**: ✅ Passed
* **client list**: ✅ Passed

**Citations Verification**:
* **02_employment_agreement_excerpt.md**: ✅ Passed

---
### Question 3 (`in_corpus`)
**Question**: What kinds of information are called out as confidential in the Bluecrest excerpt?

**Answer**:
> Confidential information includes pricing sheets, unreleased product roadmaps, and customer names marked “confidential” in writing.

**Citations**: ['02_employment_agreement_excerpt.md', '02_employment_agreement_excerpt.md', '03_hearing_notice_template.md', '06_property_lease_clause.md', '01_matter_memo_arvind_v_northfield.md']

**Facts Verification**:
* **pricing sheets**: ✅ Passed
* **product roadmaps**: ✅ Passed
* **customer names**: ✅ Passed
* **confidential**: ✅ Passed

**Citations Verification**:
* **02_employment_agreement_excerpt.md**: ✅ Passed

---
### Question 4 (`in_corpus`)
**Question**: What is the civil suit number and who are the parties in the transport invoice dispute memo?

**Answer**:
> The civil suit number is CV-2024-8812, and the parties are Arvind Mehta (the plaintiff) and Northfield Logistics Pvt. Ltd. (the defendant).

**Citations**: ['01_matter_memo_arvind_v_northfield.md', '05_counsel_notes_settlement.md', '01_matter_memo_arvind_v_northfield.md', '03_hearing_notice_template.md', '04_statute_style_excerpt_fictional.md']

**Facts Verification**:
* **CV-2024-8812**: ✅ Passed
* **Arvind Mehta**: ✅ Passed
* **Northfield Logistics**: ✅ Passed
* **invoices**: ❌ Failed
* **damaged**: ❌ Failed

**Citations Verification**:
* **01_matter_memo_arvind_v_northfield.md**: ✅ Passed

---
### Question 5 (`in_corpus`)
**Question**: Under the memo, what limitation period applies to contract claims under the fictional Riverside Code?

**Answer**:
> Three years from breach date.

**Citations**: ['01_matter_memo_arvind_v_northfield.md', '04_statute_style_excerpt_fictional.md', '05_counsel_notes_settlement.md', '02_employment_agreement_excerpt.md', '03_hearing_notice_template.md']

**Facts Verification**:
* **three years**: ✅ Passed
* **breach**: ✅ Passed

**Citations Verification**:
* **01_matter_memo_arvind_v_northfield.md**: ✅ Passed

---
### Question 6 (`in_corpus`)
**Question**: When is the next hearing in Arvind Mehta v. Northfield, and what is scheduled?

**Answer**:
> The next hearing in Arvind Mehta v. Northfield Logistics is on 15 August 2025, when the witness for the plaintiff, the billing head, is scheduled to be examined.

**Citations**: ['03_hearing_notice_template.md', '05_counsel_notes_settlement.md', '01_matter_memo_arvind_v_northfield.md', '03_hearing_notice_template.md', '01_matter_memo_arvind_v_northfield.md']

**Facts Verification**:
* **15 August 2025**: ✅ Passed
* **witness**: ✅ Passed
* **billing**: ✅ Passed

**Citations Verification**:
* **01_matter_memo_arvind_v_northfield.md**: ✅ Passed

---
### Question 7 (`in_corpus`)
**Question**: How many clear days before the listed date must parties file written arguments under the hearing notice rules?

**Answer**:
> Parties are directed to file written arguments seven clear days before the listed date.

**Citations**: ['03_hearing_notice_template.md', '01_matter_memo_arvind_v_northfield.md', '04_statute_style_excerpt_fictional.md', '03_hearing_notice_template.md', '05_counsel_notes_settlement.md']

**Facts Verification**:
* **seven**: ✅ Passed
* **clear days**: ✅ Passed
* **late filings**: ❌ Failed

**Citations Verification**:
* **03_hearing_notice_template.md**: ✅ Passed

---
### Question 8 (`in_corpus`)
**Question**: What time is case CV-2024-8812 listed, and what is it for?

**Answer**:
> Case CV-2024-8812 (Arvind Mehta v. Northfield Logistics) is listed for 11:00 a.m. and is for arguments on invoice set-off.

**Citations**: ['03_hearing_notice_template.md', '03_hearing_notice_template.md', '01_matter_memo_arvind_v_northfield.md', '01_matter_memo_arvind_v_northfield.md', '04_statute_style_excerpt_fictional.md']

**Facts Verification**:
* **11:00**: ✅ Passed
* **invoice**: ✅ Passed
* **set-off**: ✅ Passed

**Citations Verification**:
* **03_hearing_notice_template.md**: ✅ Passed

---
### Question 9 (`in_corpus`)
**Question**: What happened to case CV-2023-4401 (Lakeview Society v. City Water Board), and what is the next date?

**Answer**:
> Case CV-2023-4401 (Lakeview Society v. City Water Board) was adjourned to 22 September 2025.

**Citations**: ['03_hearing_notice_template.md', '01_matter_memo_arvind_v_northfield.md', '01_matter_memo_arvind_v_northfield.md', '05_counsel_notes_settlement.md', '03_hearing_notice_template.md']

**Facts Verification**:
* **adjourned**: ✅ Passed
* **22 September 2025**: ✅ Passed
* **water**: ✅ Passed

**Citations Verification**:
* **03_hearing_notice_template.md**: ✅ Passed

---
### Question 10 (`in_corpus`)
**Question**: For commercial suits above five lakh fictional rupees, what does Section 14 say about mediation?

**Answer**:
> For commercial suits above five lakh fictional rupees, Section 14 requires mandatory mediation for 30 days unless both parties waive in writing.

**Citations**: ['04_statute_style_excerpt_fictional.md', '05_counsel_notes_settlement.md', '03_hearing_notice_template.md', '01_matter_memo_arvind_v_northfield.md', '01_matter_memo_arvind_v_northfield.md']

**Facts Verification**:
* **mediation**: ✅ Passed
* **30 days**: ✅ Passed
* **waive**: ✅ Passed

**Citations Verification**:
* **04_statute_style_excerpt_fictional.md**: ✅ Passed

---
### Question 11 (`in_corpus`)
**Question**: If a contract fixes no interest rate, what rate may be awarded on admitted dues under Section 22?

**Answer**:
> Simple interest at 9% per year may be awarded on admitted dues from the date of demand until payment.

**Citations**: ['04_statute_style_excerpt_fictional.md', '05_counsel_notes_settlement.md', '04_statute_style_excerpt_fictional.md', '03_hearing_notice_template.md', '01_matter_memo_arvind_v_northfield.md']

**Facts Verification**:
* **9%**: ✅ Passed
* **simple interest**: ✅ Passed
* **demand**: ✅ Passed

**Citations Verification**:
* **04_statute_style_excerpt_fictional.md**: ✅ Passed

---
### Question 12 (`in_corpus`)
**Question**: What settlement offer did Northfield make in the counsel notes, and what counter-instruction did the client give?

**Answer**:
> Northfield offered to pay 70% of open invoices if Arvind drops the damage counterclaim. The client instructed to counter at 85% and keep the witness for the next hearing if no agreement is reached by 1 August 2025.

**Citations**: ['05_counsel_notes_settlement.md', '01_matter_memo_arvind_v_northfield.md', '03_hearing_notice_template.md', '04_statute_style_excerpt_fictional.md', '03_hearing_notice_template.md']

**Facts Verification**:
* **70%**: ✅ Passed
* **85%**: ✅ Passed
* **counterclaim**: ✅ Passed
* **1 August 2025**: ✅ Passed

**Citations Verification**:
* **05_counsel_notes_settlement.md**: ✅ Passed

---
### Question 13 (`in_corpus`)
**Question**: Are the settlement talks described in the counsel notes binding? What is the reminder?

**Answer**:
> The settlement talks are **without prejudice** unless a signed term sheet exists.

**Citations**: ['05_counsel_notes_settlement.md', '03_hearing_notice_template.md', '04_statute_style_excerpt_fictional.md', '01_matter_memo_arvind_v_northfield.md', '01_matter_memo_arvind_v_northfield.md']

**Facts Verification**:
* **without prejudice**: ✅ Passed
* **term sheet**: ✅ Passed

**Citations Verification**:
* **05_counsel_notes_settlement.md**: ✅ Passed

---
### Question 14 (`in_corpus`)
**Question**: Who is the lessor and lessee for Unit 4B at Harbor View Tower, and what is the monthly rent?

**Answer**:
> The lessor is Kiran Patel and the lessee is Harbor Bean Roasters OPC, with a monthly rent of ₹45,000.

**Citations**: ['06_property_lease_clause.md', '03_hearing_notice_template.md', '01_matter_memo_arvind_v_northfield.md', '02_employment_agreement_excerpt.md', '04_statute_style_excerpt_fictional.md']

**Facts Verification**:
* **Kiran Patel**: ✅ Passed
* **Harbor Bean**: ✅ Passed
* **45,000**: ✅ Passed

**Citations Verification**:
* **06_property_lease_clause.md**: ✅ Passed

---
### Question 15 (`in_corpus`)
**Question**: What is the security deposit amount, and within how many days must it be refunded after handover?

**Answer**:
> The security deposit amount is ₹1,35,000, and it is refundable within 45 days of handover if no damage beyond normal wear.

**Citations**: ['06_property_lease_clause.md', '04_statute_style_excerpt_fictional.md', '01_matter_memo_arvind_v_northfield.md', '05_counsel_notes_settlement.md', '02_employment_agreement_excerpt.md']

**Facts Verification**:
* **1,35,000**: ✅ Passed
* **45 days**: ✅ Passed

**Citations Verification**:
* **06_property_lease_clause.md**: ✅ Passed

---
### Question 16 (`in_corpus`)
**Question**: Is subletting allowed for the Harbor View lease without extra steps?

**Answer**:
> No, subletting is not allowed without written consent of the lessor.

**Citations**: ['06_property_lease_clause.md', '03_hearing_notice_template.md', '04_statute_style_excerpt_fictional.md', '05_counsel_notes_settlement.md', '01_matter_memo_arvind_v_northfield.md']

**Facts Verification**:
* **not allowed**: ✅ Passed
* **consent**: ✅ Passed

**Citations Verification**:
* **06_property_lease_clause.md**: ✅ Passed

---
### Question O1 (`out_of_corpus`)
**Question**: What is the population of Riverside city?

**Answer**:
> I could not find the answer in the provided documents.

**Citations**: []

**Facts Verification**:
* **refusal_message**: ✅ Passed

**Citations Verification**:
*No expected source files*

---
### Question O2 (`out_of_corpus`)
**Question**: What penalty applies if Priya breaches the non-compete?

**Answer**:
> I could not find the answer in the provided documents.

**Citations**: ['02_employment_agreement_excerpt.md', '04_statute_style_excerpt_fictional.md', '02_employment_agreement_excerpt.md', '05_counsel_notes_settlement.md', '01_matter_memo_arvind_v_northfield.md']

**Facts Verification**:
* **refusal_message**: ✅ Passed

**Citations Verification**:
*No expected source files*

---
### Question O3 (`out_of_corpus`)
**Question**: Who won case CV-2024-8812?

**Answer**:
> I could not find the answer in the provided documents.

**Citations**: ['03_hearing_notice_template.md', '01_matter_memo_arvind_v_northfield.md', '05_counsel_notes_settlement.md', '01_matter_memo_arvind_v_northfield.md', '03_hearing_notice_template.md']

**Facts Verification**:
* **refusal_message**: ✅ Passed

**Citations Verification**:
*No expected source files*

---
