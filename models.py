from pydantic import BaseModel
from typing import List, Dict


class DischargeSummary(BaseModel):

    patient_name: str

    admission_date: str

    discharge_date: str

    principal_diagnosis: str

    secondary_diagnoses: List[str]

    hospital_course: str

    procedures: List[str]

    discharge_medications: List[Dict]

    medication_changes: Dict

    allergies: str

    follow_up: str

    pending_results: List[str]

    discharge_condition: str

    clinician_review_flags: List[str]