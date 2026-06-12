from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_email(email_text: str):

    prompt = f"""
Analyze this customer email.

Return ONLY a valid JSON object.

Email:
{email_text}

JSON format:
{{
    "category": "",
    "sentiment": "",
    "priority": "",
    "requires_escalation": true,
    "confidence": 0.0,
    "summary": ""
    "suggested_reply": ""
}}

Confidence Rules:
- 0.95-1.00 = Very clear intent
- 0.80-0.94 = Mostly clear
- 0.70-0.79 = Some ambiguity
- Below 0.70 = Significant ambiguity, human review recommended
Generate a professional customer support reply.
Keep it concise and polite.
Categories:
- Refund Request
- Pricing Question
- Technical Issue
- SLA Complaint
- Compliance Request
- General Inquiry

Sentiment:
- Positive
- Neutral
- Negative

Priority:
- Low
- Medium
- High
- Critical
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content

        print("\nRAW RESPONSE:\n")
        print(content)
        print("\nEND RESPONSE\n")

        result = json.loads(content)

        # Safety defaults
        result.setdefault("category", "Unknown")
        result.setdefault("sentiment", "Neutral")
        result.setdefault("priority", "Medium")
        result.setdefault("requires_escalation", False)
        result.setdefault("confidence", 0.5)
        result.setdefault("summary", "")
        result.setdefault("suggested_reply", "")

        return result

    except Exception as e:

        print("ERROR:", str(e))

        return {
            "category": "Unknown",
            "sentiment": "Neutral",
            "priority": "Medium",
            "requires_escalation": False,
            "confidence": 0.0,
            "summary": f"Analysis failed: {str(e)}",
            "suggested_reply": "suggested_reply"
        }