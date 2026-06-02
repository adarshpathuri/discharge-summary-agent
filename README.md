# Discharge Summary Agent

## Overview

This project implements an agent-based AI system that generates a structured discharge summary draft from patient source documents. The goal is to assist clinicians by organizing information from multiple records while maintaining strict safety controls.

The system follows a **Plan → Act → Observe → Re-plan** workflow and treats all generated summaries as drafts that require clinician review.

The primary design principle is **clinical safety**. The agent never invents information and explicitly flags missing, pending, or conflicting data.

---

# Project Structure

```text
DischargeSummaryAgent
│
├── agent
├── tools
├── reviewer
├── learning
├── metrics
├── data
├── outputs
│
├── main.py
├── part2.py
├── models.py
├── requirements.txt
└── README.md
```

---

# Part 1 – Discharge Summary Agent

## Agent Workflow

The agent operates using an iterative workflow rather than a single-pass generation process.

```text
Plan
 ↓
Select Tool
 ↓
Execute Action
 ↓
Observe Result
 ↓
Re-plan
```

The workflow continues until all required sections of the discharge summary are completed or the maximum step limit is reached.

A hard iteration cap is enforced to prevent infinite execution.

---

## Tools

### PDF Reader Tool

Responsible for reading and extracting information from patient source documents.

### Diagnosis Tool

Extracts principal and secondary diagnoses.

### Medication Tool

Extracts discharge medications and medication-related information.

### Medication Reconciliation Tool

Compares admission and discharge medications and identifies:

* Added medications
* Removed medications
* Modified medications
* Undocumented changes

### Conflict Detection Tool

Detects conflicting information across source documents.

### Escalation Tool

Flags situations requiring clinician review.

---

## Safety Guardrails

Clinical safety is prioritized throughout the system.

### No Fabrication

The agent never invents or guesses clinical information.

If required information cannot be found, it is marked as:

```text
MISSING - Clinician Review Required
```

### Missing and Pending Information

The system explicitly identifies:

* Missing data
* Pending laboratory results
* Incomplete documentation

### Conflict Handling

When contradictory information is detected, the agent:

1. Flags the issue.
2. Records it in clinician review flags.
3. Avoids automatically selecting one version over another.

### Human Review

Every generated discharge summary is treated as a draft and requires clinician validation before use.

---

## Observability

The system produces a detailed execution trace.

Each step records:

* Plan
* Action
* Observation
* Next Decision

This improves transparency and makes the agent's behavior easy to inspect and debug.

---

## Output Files

### summary.json

Structured discharge summary containing:

* Patient demographics
* Diagnoses
* Procedures
* Medications
* Follow-up instructions
* Pending results
* Discharge condition
* Review flags

### trace.log

Complete agent execution trace.

---

# Part 2 – Learning From Doctor Edits

## Objective

In real clinical workflows, doctors review and modify generated discharge summaries.

These edits contain valuable feedback that can be used to improve future drafts.

Since real clinician-edited data is unavailable, a simulated reviewer is used.

---

## Simulated Doctor

A simulated doctor reviews the generated summary and applies a consistent editing policy.

This creates:

```text
Draft Summary
      ↓
Doctor Edited Summary
```

The edited version serves as feedback for the learning process.

---

## Reward Design

The difference between the draft and edited version is converted into a reward score.

The reward is based on similarity between the two documents.

Higher reward:

* Fewer edits required
* Better draft quality

Lower reward:

* More edits required
* Greater correction burden

---

## Learning Mechanism

The system stores observed corrections in a correction memory.

Workflow:

```text
Draft
 ↓
Doctor Edit
 ↓
Reward Calculation
 ↓
Correction Memory
 ↓
Future Improvement
```

This allows the system to learn from previous corrections and gradually reduce editing effort.

---

## Example Improvement

| Iteration | Reward |
| --------- | ------ |
| 1         | 0.55   |
| 2         | 0.68   |
| 3         | 0.77   |
| 4         | 0.86   |
| 5         | 0.93   |

The increasing reward demonstrates that the system requires fewer edits over time.

---

# How to Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Part 1

```bash
py main.py
```

Generated outputs:

```text
outputs/summary.json
outputs/trace.log
```

## Run Part 2

```bash
py part2.py
```

Generated outputs:

```text
outputs/doctor_edited.json
learning/correction_memory.json
```

---

# Limitations

* Uses synthetic patient data only.
* Simulated reviewer is used instead of real clinician feedback.
* OCR support for scanned PDFs can be further improved.
* Learning memory is intentionally simple and designed for demonstration purposes.

---

# Future Improvements

Given additional time, the following enhancements would be valuable:

* OCR-based document ingestion
* Real clinician feedback integration
* Drug interaction checking
* More advanced learning strategies
* Improved conflict detection
* Expanded medication safety checks

---

# Conclusion

This project demonstrates an agent-based approach to discharge summary generation with a strong focus on safety, transparency, traceability, and human oversight. The Part 2 learning loop shows how clinician feedback can be transformed into measurable improvements while preserving the no-fabrication guarantees established in Part 1.
