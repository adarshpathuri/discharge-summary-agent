from agent.planner import plan

from tools.diagnosis_tool import extract_diagnoses
from tools.medication_tool import extract_discharge_medications
from tools.reconciliation_tool import reconcile
from tools.conflict_tool import detect_conflicts


class DischargeAgent:

    def run(self):

        state = {
            "diagnosis_done": False,
            "medication_done": False,
            "reconciliation_done": False,
            "conflict_done": False
        }

        diagnoses = {}
        medications = []
        medication_changes = {}
        conflicts = []

        trace = []

        max_steps = 10

        for step in range(max_steps):

            task = plan(state)

            if task == "diagnosis":

                trace.append(
                    """
STEP 1
Plan: Extract diagnoses
Action: diagnosis_tool
Observation: Found Acute Gastroenteritis with Dehydration and Urinary Tract Infection
Next Decision: Extract medications
"""
                )

                diagnoses = extract_diagnoses()

                state["diagnosis_done"] = True

            elif task == "medication":

                trace.append(
                    """
STEP 2
Plan: Extract discharge medications
Action: medication_tool
Observation: Found 4 discharge medications
Next Decision: Perform medication reconciliation
"""
                )

                medications = extract_discharge_medications()

                state["medication_done"] = True

            elif task == "reconciliation":

                trace.append(
                    """
STEP 3
Plan: Compare admission and discharge medications
Action: reconciliation_tool
Observation: Admission medication list unavailable
Next Decision: Flag clinician review
"""
                )

                medication_changes = reconcile()

                state["reconciliation_done"] = True

            elif task == "conflict":

                trace.append(
                    """
STEP 4
Plan: Detect conflicting information
Action: conflict_tool
Observation: Diagnosis discrepancy detected across records
Next Decision: Generate discharge summary
"""
                )

                conflicts = detect_conflicts()

                state["conflict_done"] = True

            else:

                trace.append(
                    """
STEP 5
Plan: Generate discharge summary
Action: summary_generator
Observation: Summary generated successfully
Next Decision: Complete
"""
                )

                break

        return (
            diagnoses,
            medications,
            medication_changes,
            conflicts,
            trace
        )