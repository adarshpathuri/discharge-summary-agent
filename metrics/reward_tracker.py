import json
from difflib import SequenceMatcher


def calculate_reward(
        original_summary,
        edited_summary
):

    original = json.dumps(
        original_summary,
        sort_keys=True
    )

    edited = json.dumps(
        edited_summary,
        sort_keys=True
    )

    similarity = SequenceMatcher(
        None,
        original,
        edited
    ).ratio()

    return round(similarity, 3)