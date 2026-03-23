from openai import OpenAI
import json
from config import MODEL

client = OpenAI()

def call_llm(prompt: str) -> str:
    structured_prompt = f"""
    {prompt}

    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": structured_prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content


def safe_json_loads(text: str):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        print("⚠️ Invalid JSON from AI:", text)
        return []