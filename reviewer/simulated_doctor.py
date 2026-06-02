import copy


class SimulatedDoctor:

    def review(self, summary):

        edited = copy.deepcopy(summary)

        # Hidden Rule 1
        if edited["allergies"] == \
           "MISSING - Clinician Review Required":

            edited["allergies"] = \
                "REVIEW NEEDED"

        # Hidden Rule 2
        if edited["clinician_review_flags"]:

            edited["clinician_review_flags"].append(
                "Confirm diagnosis before finalization."
            )

        # Hidden Rule 3
        if edited["medication_changes"]["needs_review"]:

            edited["medication_changes"][
                "needs_review"
            ].append(
                "Medication change reason undocumented."
            )

        return edited