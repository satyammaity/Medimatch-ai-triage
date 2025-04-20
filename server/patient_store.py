import uuid
from datetime import datetime

# In-memory store for patients
patients = []

def add_patient(name, severity, symptoms, pdf_filename):
    patient = {
        "id": str(uuid.uuid4()),
        "name": name,
        "severity": severity,
        "symptoms": symptoms,
        "pdf": pdf_filename,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    patients.append(patient)

    # Optional: sort so high severity appears first
    patients.sort(key=lambda x: ["High", "Medium", "Low"].index(x["severity"]))
    return patient

def get_all_patients():
    return patients