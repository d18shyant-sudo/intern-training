import httpx 
import os
from dotenv import load_dotenv
import json
from schema.Model import Employee,Salary
import structlog
import uuid
load_dotenv()
URL = os.getenv("URL")
API = os.getenv("OPEN_ROUTER_API")
from structlog.contextvars import (
    bind_contextvars,
    clear_contextvars
)
structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ]
)

logger = structlog.get_logger()
model = "liquid/lfm-2.5-2.6b:free"
headers = {
    "Authorization" :f"Bearer {API}",
    "Content-Type":"application/json"
}
system_prompt = """Use the available tools to answer the user's request."""
def get_employees(emp_id):
    result = httpx.post("http://127.0.0.1:8000/service/get-employee",json={"emp_id":emp_id},timeout=30)
    return result.json()
def calculate_bonus(salary):
    result = httpx.post("http://127.0.0.1:8000/service/calculate-salary",json={"salary":salary},timeout=30)
    return result.json()
tools = [{"type":"function","function":{ "name":"get_employee",
               "description":"Fetch Employee by an employee id .",
               "parameters":Employee.model_json_schema()}},  {"type":"function",
          "function":{
               "name":"calculate_bonus",
               "description":"Calculate an employee Bonus.",
               "parameters":Salary.model_json_schema()}  
               }]
tool_registry = {"get_employee":get_employees,"calculate_bonus":calculate_bonus}
messages = []
messages.append({"role":"system","content":system_prompt})
while True:
    prompt =  input(">>>")
    if prompt == "exit":
        break
    clear_contextvars()

    request_id = str(uuid.uuid4())

    bind_contextvars(
        request_id=request_id
    )

    logger.info("request_started")
    messages.append({"role":"user","content":prompt})
    request = {
        "model":model,
        "messages":messages,
        "tools":tools
    }
    logger.info("calling_llm")
    response = httpx.post(url=URL,headers=headers,json=request,timeout=30).json()
    message = response["choices"][0]["message"]
    for toolcall in message.get("tool_calls"):
        function_name = toolcall["function"]["name"]
        logger.info(
            "tool_call_started",
            tool_name=function_name
        )
        function = tool_registry[function_name]
        arguments = json.loads(toolcall["function"]["arguments"])
        result =function(**arguments)
        print(result)
        logger.info(
            "tool_call_completed",
            tool_name=function_name
        )
        messages.append({"role":"tool","tool_call_id":toolcall["id"],"result":json.dumps(result)})
        logger.info("request_completed")