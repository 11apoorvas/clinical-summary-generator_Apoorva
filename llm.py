# import os
# import json
# from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def generate_summary(prompt: str) -> dict:
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.2
#     )
#     return json.loads(response.choices[0].message.content)

def generate_summary(prompt: str) -> dict:
    """
    Mock LLM response for demo & testing.
    """
    return {
        "summary": [
            {
                "statement": "Patient has a primary diagnosis of hypertension.",
                "source": "diagnoses.csv"
            },
            {
                "statement": "Recent blood pressure readings show mild elevation.",
                "source": "vitals.csv"
            },
            {
                "statement": "Patient is compliant with prescribed medications.",
                "source": "medications.csv"
            },
            {
                "statement": "No active wounds reported.",
                "source": "wounds.csv"
            },
            {
                "statement": "Functional status indicates independent ambulation.",
                "source": "oasis.csv"
            }
        ]
    }
