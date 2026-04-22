import requests

def explain_sql(sql: str) -> str:
    prompt = f"""
Explain the following SQL query in simple business terms.

Make it:
- Easy to understand
- Non-technical
- Focus on what insight it gives

SQL:
{sql}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"].strip()

    except Exception as e:
        print("Explanation Error:", e)
        return "Could not generate explanation."