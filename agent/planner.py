def plan(state):

    if not state["diagnosis_done"]:
        return "diagnosis"

    if not state["medication_done"]:
        return "medication"

    if not state["reconciliation_done"]:
        return "reconciliation"

    if not state["conflict_done"]:
        return "conflict"

    return "complete"