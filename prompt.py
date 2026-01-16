def build_prompt(context: str) -> str:
    return f"""
You are a licensed home health clinician.

Generate a concise, evidence-based clinical summary using ONLY the data below.

Focus on:
- Primary diagnoses
- Recent vital sign trends
- Active wounds
- Medication adherence or changes
- Functional status (OASIS)

STRICT RULES:
1. Do NOT hallucinate or infer missing data.
2. Every statement MUST include a citation.
3. Return ONLY valid JSON in the following format:

{{
  "summary": [
    {{
      "statement": "...",
      "source": "CSV file name",
      "date": "if available"
    }}
  ]
}}

PATIENT DATA:
{context}
"""
