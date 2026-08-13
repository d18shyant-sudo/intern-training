import httpx
import os
from dotenv import load_dotenv
import json
load_dotenv()
api_key = os.getenv("OPEN_ROUTER_API")
text = "What is the use of ai ?"*1300000
model_name="liquid/lfm-2.5-2.6b:free"
headers = {"Authorization":f"Bearer {api_key}","Content-Type":"application/json"}
message =[{"role":"user","content":text}]
response = httpx.post("https://openrouter.ai/api/v1/chat/completions",headers=headers,json={"model":model_name,"messages":message},timeout=30)
data = response.json()
print(data)