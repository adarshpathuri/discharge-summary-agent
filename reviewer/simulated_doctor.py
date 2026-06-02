import copy


class SimulatedDoctor:

    def review(self, summary):

        edited = copy.deepcopy(summary)

        corrections = []

        if edited["allergies"] == \
           "MISSING - Clinician Review Required":

            edited["allergies"] = "REVIEW NEEDED"

            corrections.append(
                {
                    "field": "allergies",
                    "value": "REVIEW NEEDED"
                }
            )

        if edited["clinician_review_flags"]:

            edited["clinician_review_flags"].append(
                "Confirm diagnosis before finalization."
            )

            corrections.append(
                {
                    "field": "diagnosis_conflict",
                    "value":
                    "Confirm diagnosis before finalization."
                }
            )

        return edited, corrections