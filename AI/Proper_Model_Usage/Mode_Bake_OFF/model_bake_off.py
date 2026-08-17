import httpx 
import json
from dotenv import load_dotenv
import os
import time
import ollama
from tenacity import retry,wait_exponential,stop_after_attempt
load_dotenv()
API_KEY = os.getenv("OPEN_ROUTER_API")
URL = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}
model_1 = "liquid/lfm-2.5-2.6b:free"
model_2 = "nvidia/nemotron-nano-9b-v2:free"
model_3 = "dots-studio/dots-3-note-preview:free"
model_4 = "openai/gpt-oss-20b:free"
local_model = "qwen2.5:7b"
models = []
models.extend([model_1,model_2,model_3,model_4,local_model])
prompt_1 = "Explain what an API is in simple terms."
prompt_2 = "give a 3 steps to reduce the global warming"
prompt_3 =  "Write a professional email asking for a meeting."
prompt_4 = "If a product costs ₹2,000 and has a 15% discount, what is the final price?"
prompt_5 =  "Write a Python function that checks whether a number is prime."
prompts = [] 
prompts.extend([prompt_1,prompt_2,prompt_3,prompt_4,prompt_5])
latency = []
def local_model_call(model_name,prompt):
    response = ollama.chat(model=model_name,messages=[{"role":"user","content":prompt}])
    output = response["message"]["content"]
    return output
@retry(stop=stop_after_attempt(4),wait=wait_exponential(multiplier=1,min=1,max=10))
def request(model,prompt):
    response = httpx.post(URL,headers=headers,json={"model":model,"messages":[{"role":"user","content":prompt}]},timeout=30).json()
    result = response["choices"][0]["message"]["content"]
    return result
for model in models:
    print("Model Name:",model)
    start = time.perf_counter()
    for prompt in prompts:
        try:
            if model == local_model:
                output = local_model_call(model_name=model,prompt=prompt)
            else:
                output = request(model=model,prompt=prompt)
            print(output)
        except Exception as e:
            print(e)
    end = time.perf_counter()
    current_model = {}
    current_model["model_name"] = model
    current_model["time_taken"] = end-start
    latency.append(current_model)
print(latency)