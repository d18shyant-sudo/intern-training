import json
import os
import httpx
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("OPEN_ROUTER_API")
model_name = "nvidia/nemotron-nano-9b-v2:free"
message = [{"role":"user","content":"write essay about the global warming ?"}]
temperature = 1.0
headers={"Authorization":f"Bearer {API_KEY}","Content-Type":"application/json"}
response = httpx.post("https://openrouter.ai/api/v1/chat/completions",
headers=headers,json={"model":model_name,"temperature":temperature,"messages":message},timeout=30)
data = response.json()
print(data["choices"][0]["message"]["content"])