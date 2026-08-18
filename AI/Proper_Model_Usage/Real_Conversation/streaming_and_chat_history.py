import os
import httpx
from dotenv import load_dotenv
import json
load_dotenv()
API = os.getenv("OPEN_ROUTER_API")
URL = os.getenv("URL")
model_1 = "dots-studio/dots-3-note-preview:free"
model_2 = "openai/gpt-oss-20b:free"
models = []
models.extend([model_1,model_2])
PRICE = 0.00123
headers = {
    "Authorization":f"Bearer {API}",
    "Content-Type":"application/json"
}
messages =[]
exit = False
for model in models:
    if exit:
        break
    try:
        while not exit:
            prompt = input("\nUser>>>")
            if prompt.lower() == "exit":
                exit = True
                break
            messages.append({"role":"user","content":prompt})
            request = {
            "model":model,
            "messages":messages,
            "stream":True
            }
            answer = ""
            print("\nAssistant>>>",end="",flush=True)
            token = 0
            with httpx.stream("POST",url=URL,headers=headers,json=request,timeout=30) as response:
                for line in response.iter_lines():
                    if not line:
                        continue
                    if not line.startswith("data:"):
                        continue
                    result = line[6:]
                    if result == "[DONE]":
                        break
                    data = json.loads(result)
                    content = data["choices"][0]["delta"].get("content")
                    if data.get("usage"):
                        token = data["usage"].get("total_tokens")
                    if content: 
                        print(content, end="", flush=True)
                        answer += content
            print(f"(cost:{token*PRICE})")
            messages.append({"role":"assistant","content":answer})
            print()
    except Exception as e :
        print(e)
        continue