

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
