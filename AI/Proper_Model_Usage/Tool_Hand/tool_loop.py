import json
import os
from dotenv import load_dotenv
from tools.tools import get_employee,calculate_bonus
from schema.Model import Employee,Salary
import httpx
load_dotenv()
URL = os.getenv("URL")
API = os.getenv("OPEN_ROUTER_API")
headers = {
    "Authorization":f"Bearer {API}",
    "Content-Type":"application/json"
}
model = "dots-studio/dots-3-note-preview:free"
system_prompt = """Use the available tools to answer the user's request."""
MAX_ITERATION =3
tools = [{"type":"function",
          "function":{
               "name":"get_employee",
               "description":"Fetch Employee by an employee id .",
               "parameters":Employee.model_json_schema()}},
               {"type":"function",
          "function":{
               "name":"calculate_bonus",
               "description":"Calculate an employee Bonus.",
               "parameters":Salary.model_json_schema()}  
               }]
tools_registry = {"get_employee":get_employee,"calculate_bonus":calculate_bonus}
attempt = 1
messages= []
messages.append({"role":"system","content":system_prompt})
while  True:
    prompt = input(">>>")
    if prompt == "exit":
        break
    messages.append({
            "role":"user",
            "content":prompt
        })
    request = {
            "model":model,
            "messages":messages,
            "tools":tools
        }
    if attempt<=MAX_ITERATION :
        attempt+=1
        response = httpx.post(url=URL,headers=headers,json=request,timeout=30).json()
        message = response["choices"][0]["message"]
        for toolcall in message.get("tool_calls" ):
            function_name = toolcall["function"]["name"]
            arguments = json.loads(toolcall["function"]["arguments"])
            function = tools_registry[function_name]
            result = function(**arguments)
            print(result)
            messages.append({"role":"tool","tool_call_id":toolcall["id"],"content":json.dumps(result)})
            print(messages)
    else:
        print("max attempts is reached")        
        break