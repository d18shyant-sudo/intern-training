import json
import os
import httpx
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("OPEN_ROUTER_API")
model_name = "nvidia/nemotron-nano-9b-v2:free"
message = [{"role": "system","content": "/no_think"},{"role":"user","content":"write about the global warming ?"}]
temperature = 1.0
max_token = 20
headers={"Authorization":f"Bearer {API_KEY}","Content-Type":"application/json"}
response = httpx.post("https://openrouter.ai/api/v1/chat/completions",
headers=headers,json={"model":model_name,"reasoning":{"effort":"low"},"temperature":temperature,"max_tokens":max_token,"messages":message},timeout=30)
data = response.json()
# print(data)
print(data["choices"][0]["message"]["content"])