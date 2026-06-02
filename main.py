import json

from agent.discharge_agent import (
    DischargeAgent
)

from models import DischargeSummary

from learning.correction_memory import (
    get_learned_corrections
)

try:

    # Run Agent

    agent = DischargeAgent()

    (
        diagnoses,
        medications,
        medication_changes,
        conflicts,
        trace
    ) = agent.run()

    # Create Summary

    summary = DischargeSummary(

        patient_name=
        "MISSING - Clinician Review Required",

        admission_date=
        "MISSING - Clinician Review Required",

        discharge_date=
        "MISSING - Clinician Review Required",

        principal_diagnosis=
        diagnoses["principal"],

        secondary_diagnoses=
        diagnoses["secondary"],

        hospital_course=
        (
            "Patient treated with IV fluids, "
            "IV antibiotics, antiemetics "
            "and proton pump inhibitors."
        ),

        procedures=[
            "IV Therapy"
        ],

        discharge_medications=
        medications,

        medication_changes=
        medication_changes,

        allergies=
        "MISSING - Clinician Review Required",

        follow_up=
        (
            "Review if fever, vomiting "
            "or loose stools recur."
        ),

        pending_results=[
            "Urine Culture and Sensitivity"
        ],

        discharge_condition=
        "Hemodynamically Stable",

        clinician_review_flags=
        conflicts
    )

    # Apply Learned Corrections

    memory = get_learned_corrections()

    if "allergies" in memory:

        summary.allergies = \
            memory["allergies"]

    # Save Summary

    with open(
        "outputs/summary.json",
        "w"
    ) as f:

        json.dump(
            summary.model_dump(),
            f,
            indent=4
        )

    # Save Trace

    with open(
        "outputs/trace.log",
        "w"
    ) as f:

        for item in trace:

            f.write(item + "\n")

    print(
        "Summary Generated Successfully"
    )

except Exception as e:

    print(
        f"Agent Failed: {e}"
    )