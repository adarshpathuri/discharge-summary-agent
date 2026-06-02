# Discharge Summary Agent

## Project Overview

This project generates a structured discharge summary from patient records using an agent-based workflow.

The agent follows:

Plan → Act → Observe → Re-plan

and uses multiple tools to extract information, reconcile medications, detect conflicts, and generate a discharge summary.

---

## Project Structure

```text
DischargeSummaryAgent
│
├── agent
├── tools
├── data
├── outputs
├── main.py
├── models.py
└── README.md
```

---

## Tools

### PDF Reader Tool
Reads patient PDF documents.

### Diagnosis Tool
Extracts diagnosis information.

### Medication Tool
Extracts discharge medications.

### Reconciliation Tool
Compares medication information.

### Conflict Tool
Identifies conflicting information.

### Escalation Tool
Flags issues requiring clinician review.

---

## Agent Workflow

1. Extract Diagnoses
2. Extract Medications
3. Perform Medication Reconciliation
4. Detect Conflicts
5. Generate Summary

---

## Output Files

### summary.json

Structured discharge summary.

### trace.log

Agent reasoning trace showing:

- Plan
- Action
- Observation
- Next Decision

---

## Assumptions

- Missing information is never fabricated.
- Missing values are marked as:
  "MISSING - Clinician Review Required"

---

## How To Run

```bash
pip install -r requirements.txt
py main.py
```

---

## Limitations

- Medication reconciliation uses available information only.
- Missing source information requires clinician review.