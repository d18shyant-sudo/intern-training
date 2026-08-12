import os
import json
import httpx
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPEN_ROUTER_KEY")

headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json",
}


response_1 = httpx.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json={
        "model": "nvidia/nemotron-nano-9b-v2:free",
        "messages": [
            {
                "role": "user",
                "content": "why e20 petrol receives a good review among all indians and how indian government aids in it?"
            }
        ]
    },
    timeout=30
)
print("Status:", response_1.status_code)
print("Response:", response_1.text)
response_1.raise_for_status()
data_1 = response_1.json()


response_2 = httpx.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json={
        "model": "nvidia/nemotron-nano-9b-v2:free",
        "messages": [
            {
                "role": "user",
                "content": "who is the ceo of Engrox company ?"
            }
        ]
    },
    timeout=30
)

response_2.raise_for_status()
data_2 = response_2.json()


response_3 = httpx.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json={
        "model": "nvidia/nemotron-nano-9b-v2:free",
        "messages": [
            {
                "role": "user",
                "content": "Give the citations for ajay lakshmanan's bussiness growth "
            }
        ]
    },
    timeout=30
)

response_3.raise_for_status()
data_3 = response_3.json()


print(json.dumps(data_1, indent=4))
print(json.dumps(data_2, indent=4))
print(json.dumps(data_3, indent=4))