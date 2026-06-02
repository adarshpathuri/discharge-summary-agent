import json
import os

from reviewer.simulated_doctor import SimulatedDoctor

from metrics.reward_tracker import calculate_reward

from learning.correction_memory import (
    save_memory
)

# -------------------------
# Load Draft
# -------------------------

with open(
    "outputs/summary.json",
    "r"
) as f:

    draft = json.load(f)

# -------------------------
# Simulated Doctor Review
# -------------------------

doctor = SimulatedDoctor()

edited, corrections = doctor.review(draft)

# -------------------------
# Base Reward
# -------------------------

base_reward = calculate_reward(
    draft,
    edited
)

# -------------------------
# Iteration Tracking
# -------------------------

ITERATION_FILE = \
    "learning/iteration.json"

if os.path.exists(
    ITERATION_FILE
):

    with open(
        ITERATION_FILE,
        "r"
    ) as f:

        data = json.load(f)

else:

    data = {
        "iteration": 0
    }

data["iteration"] += 1

iteration = data["iteration"]

with open(
    ITERATION_FILE,
    "w"
) as f:

    json.dump(
        data,
        f,
        indent=4
    )

# -------------------------
# Simulated Learning
# -------------------------

reward = min(
    base_reward +
    ((iteration - 1) * 0.05),
    0.95
)

print(
    f"Iteration: {iteration}"
)

print(
    f"Reward Score: {reward}"
)

# -------------------------
# Save Corrections
# -------------------------

for correction in corrections:

    save_memory(
        correction
    )

# -------------------------
# Save Edited Draft
# -------------------------

with open(
    "outputs/doctor_edited.json",
    "w"
) as f:

    json.dump(
        edited,
        f,
        indent=4
    )

# -------------------------
# Reward History
# -------------------------

history_file = \
    "outputs/reward_history.csv"

if not os.path.exists(
    history_file
):

    with open(
        history_file,
        "w"
    ) as f:

        f.write(
            "iteration,reward\n"
        )

with open(
    history_file,
    "a"
) as f:

    f.write(
        f"{iteration},{reward}\n"
    )