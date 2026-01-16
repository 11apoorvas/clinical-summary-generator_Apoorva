from fastapi import FastAPI, HTTPException


from .data_loader import DataLoader
from .prompt import build_prompt
from .llm import generate_summary


app = FastAPI(title="Clinical Summary Generator API")
loader = DataLoader()

@app.post("/generate_summary")
def generate_summary_api(patient_id: int):
    patient_data = loader.get_patient_data(patient_id)

    if all(df.empty for df in patient_data.values()):
        raise HTTPException(status_code=404, detail="Patient not found")

    context = ""
    for table_name, df in patient_data.items():
        context += f"\n\n{table_name.upper()}:\n"
        context += df.to_string(index=False)

    prompt = build_prompt(context)
    return generate_summary(prompt)
