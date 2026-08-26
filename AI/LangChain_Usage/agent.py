import os
import httpx
import json
from dotenv import load_dotenv
from schema.Model import Employee,Salary
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,ToolMessage,SystemMessage
load_dotenv()
api_key = os.getenv("OPEN_ROUTER_API")
url = os.getenv("URL")
model = "nvidia/nemotron-3-ultra-550b-a55b:free"
@tool(args_schema=Employee)
def get_employees(emp_id):
    """Fetch Employee by and employee id"""
    result = httpx.post("http://127.0.0.1:8000/service/get-employee",json={"emp_id":emp_id},timeout=30)
    return result.json()
@tool(args_schema=Salary)
def calculate_bonus(salary):
    """calculate an employee bonus"""
    result = httpx.post("http://127.0.0.1:8000/service/calculate-salary",json={"salary":salary},timeout=30)
    return result.json()
tools = [get_employees,calculate_bonus]
model = ChatOpenAI(model=model,api_key=api_key,base_url=url,temperature=0)
model_with_tools = model.bind_tools(tools)
messages = [SystemMessage(content="Use the available tools to answer the user's request.")]
while True:
    prompt = input(">>>")
    if prompt == "exit":
        break
    messages.append(HumanMessage(content=prompt))
    response = model_with_tools.invoke(messages)
    messages.append(response)
    for tool_call in response.tool_calls:
        tool_name = tool_call["name"]
        tool_map = {
            "get_employees" : get_employees,
            "calculate_bonus" :calculate_bonus
        }
        selected_tool = tool_map[tool_name]
        arguments = tool_call["args"]
        result = selected_tool.invoke(arguments)
        messages.append(ToolMessage(content=json.dumps(result),tool_call_id=tool_call["id"]))
    if response.tool_calls:
        final_response = model_with_tools.invoke(messages)
        messages.append(final_response)
        print("Assistant")
        print(final_response.content)