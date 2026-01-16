import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

class DataLoader:
    def __init__(self):
        self.diagnoses = pd.read_csv(DATA_DIR / "diagnoses.csv")
        self.medications = pd.read_csv(DATA_DIR / "medications.csv")
        self.vitals = pd.read_csv(DATA_DIR / "vitals.csv")
        self.notes = pd.read_csv(DATA_DIR / "notes.csv")
        self.wounds = pd.read_csv(DATA_DIR / "wounds.csv")
        self.oasis = pd.read_csv(DATA_DIR / "oasis.csv")
        pass

    def get_patient_data(self, patient_id: int):
        return {
            "diagnoses": self.diagnoses[self.diagnoses.patient_id == patient_id],
            "medications": self.medications[self.medications.patient_id == patient_id],
            "vitals": self.vitals[self.vitals.patient_id == patient_id],
            "notes": self.notes[self.notes.patient_id == patient_id],
            "wounds": self.wounds[self.wounds.patient_id == patient_id],
            "oasis": self.oasis[self.oasis.patient_id == patient_id],
        }
