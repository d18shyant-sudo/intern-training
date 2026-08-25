import httpx
import os
import json
import uuid
from datetime import datetime
import httpx
from dotenv import load_dotenv
from schema.conversation import ConversationRequest
load_dotenv()
URL = os.getenv("URL")
API= os.getenv("OPEN_ROUTER_API")
headers = {
    "Authorization" : f"Bearer {API}",
    "Content-Type" :  "application/json"
}
model = "nvidia/nemotron-3.5-lightning:free"
messages = []
while True:
    user =  str(uuid.uuid4())
    prompt = input(">>>")
    if prompt == "exit":
        break
    messages.append({"role":"user","content":prompt})
    request = {
        "model":model,
        "messages":messages
    }
    response = httpx.post(url=URL,headers=headers,json=request,timeout=30).json()
    print(response)
    result = response["choices"][0]["message"]["content"]
    print(result)
    messages.append({"role":"assistant","content":result})
    print(messages)
    argument = {
            "req_id":str(uuid.uuid4()),
            "user_id":user, # genereated user_id directly just for experimenting purpouse
            "created_at":datetime.now(),
            "model_name":model,
            "prompt":prompt,
            "response":result,
            "created_by":user
        }
    arguments = ConversationRequest.model_validate(argument).model_dump(mode="json")
    httpx.post("http://127.0.0.1:8000/api/v1/post-conversation",json=arguments,timeout=30)