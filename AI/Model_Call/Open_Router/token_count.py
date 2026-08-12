import os 
import json 
import httpx
from dotenv import load_dotenv
from transformers import AutoTokenizer 
load_dotenv()
key = os.getenv("OPEN_ROUTER_KEY")
model_name = "nvidia/nemotron-nano-9b-v2:free"
model_name_local = "nvidia/NVIDIA-Nemotron-Nano-9B-v2"
token_cost = 0.025
message = [
    {
        "role": "user",
        "content": "how to use the ai and tells is pros and cons?"
    }
]

response = httpx.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    },
    json={
        "model": model_name,
        "messages": message
    },
    timeout=30
)

data = response.json()
actual_prompt_token = data["usage"]["prompt_tokens"]
print("Actual prompt token:",actual_prompt_token)

tokenizer = AutoTokenizer.from_pretrained(
    model_name_local,
    trust_remote_code=True
)

tokens = tokenizer.apply_chat_template(
    message,
    tokenize=True,
    add_generation_prompt=True
)
estimated_prompt_token = len(tokens["input_ids"])
print("Estimated prompt token:",estimated_prompt_token)
print(f"Cost of prompt token(in inr):{actual_prompt_token*token_cost*95}₹")
print(f"Cost of prompt token(in usd):{estimated_prompt_token*token_cost}$")