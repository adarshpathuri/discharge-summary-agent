import json
import os


MEMORY_FILE = \
    "learning/correction_memory.json"


def save_memory(correction):

    memory = []

    if os.path.exists(MEMORY_FILE):

        with open(
            MEMORY_FILE,
            "r"
        ) as f:

            memory = json.load(f)

    memory.append(correction)

    with open(
        MEMORY_FILE,
        "w"
    ) as f:

        json.dump(
            memory,
            f,
            indent=4
        )


def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return []

    with open(
        MEMORY_FILE,
        "r"
    ) as f:

        return json.load(f)