import json
import os

MEMORY_FILE = "learning/correction_memory.json"


def save_memory(correction):

    memory = load_memory()

    memory.append(correction)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def get_learned_corrections():

    memory = load_memory()

    learned = {}

    for item in memory:

        if "field" in item:
            learned[item["field"]] = item["value"]

    return learned