import os
from groq import Groq

def generate_insights(analysis: dict, business_context: str = "Sales") -> str:

    client = Groq(api_key="YOUR_GROQ_API_KEY")
    prompt = (
        f"You are a senior business data analyst.\n"
        f"Analyze the following dataset summary and generate a professional business report.\n\n"
        f"Business Context: {business_context}\n\n"
        f"Dataset Info:\n"
        f"- Shape: {analysis['shape']}\n"
        f"- Columns: {analysis['columns']}\n"
        f"- Null Values: {analysis['nulls']}\n\n"
        f"Statistical Summary:\n{analysis['summary']}\n\n"
        f"Sample Data:\n{analysis['sample']}\n\n"
        f"Generate a structured business report with:\n"
        f"1. Executive Summary (3-4 lines)\n"
        f"2. Key Findings (5 bullet points)\n"
        f"3. Trends and Patterns\n"
        f"4. Risks or Data Quality Issues\n"
        f"5. Actionable Recommendations (3-5 points)\n\n"
        f"Be specific, use numbers where possible, professional tone."
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500
    )

    return response.choices[0].message.content