# clinical-summary-generator_Apoorva
it is python app  that generates clinical summaries from CSV-based  data using a backend API and a simple UI.

Overview : 
Loads patient data from CSV files.
Filters records by patient_id.
Generates clinical summary that includes a source citation.
It Uses a LLM (no external API required). LLM responses are mocked for cost control.
The app supports easy integration with real LLMs.

Architecture
Backend - FastAPI
Frontend - Streamlit
Data Processing - Pandas

Running the app
python -m venv venv
.\venv\Scripts\activate
python -m pip install -r requirements.txt
python -m uvicorn backend.main:app --reload
python -m streamlit run frontend/app.py

Output sample :
Clinical summary 
• Recent blood pressure readings show mild elevation.

Source: vitals.csv | Date: N/A
