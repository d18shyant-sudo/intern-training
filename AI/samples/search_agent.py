import ollama
from pydantic import BaseModel
import json

class ExpenseClaim(BaseModel):
    employee_name: str
    amount: float
    category: str

schema = ExpenseClaim.model_json_schema()
system_prompt = f"""
You are an AI assistant.

Extract the user's request and return JSON that matches
the following JSON Schema.
Context:
- Current user: EMP001 (Robert)

Instructions:
- Resolve third-person pronouns using the conversation.
- Treat "I", "me", and "my" as the current authenticated user.
- If a pronoun is ambiguous, do not guess. Ask for clarification.
- Produce output matching the provided schema.

Schema:
{json.dumps(schema, indent=2)}

Return ONLY valid JSON.
"""

while True:
    user_input = input(">>> ")

    response = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    request = json.loads(response["message"]["content"])
    print(request)