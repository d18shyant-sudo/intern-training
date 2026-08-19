import json
import os
import httpx
from dotenv import load_dotenv
from model import Employee
from pydantic import ValidationError
load_dotenv()
URL = os.getenv("URL")
API = os.getenv("OPEN_ROUTER_API")
model = "dots-studio/dots-3-note-preview:free"
headers = {
    "Authorization":f"Bearer {API}",
    "Content-Type":"application/json"
}
schema = json.dumps(Employee.model_json_schema(),indent=2)
MAX_ATTEMPT = 3
def  validate_json(e):
    return f"""Your previous response did not match the required Employee schema.

Validation error:
{e}

Correct your previous JSON.

Return ONLY the corrected JSON.
Use EXACTLY the field names from the Employee schema.
Do not add explanations.
"""
system_prompt = f"""
Extract employee information from the user's input.

Return an Employee object matching the provided schema.
use the field names only in schema.
Schema:
    {schema}
Only use information explicitly provided by the user.
If an optional field is not provided, use null.
Do not invent missing information."""
attempt = 1
prompt = input(">>>")
message = [{
        "role":"system",
    "content":system_prompt},
    {
    "role":"user",
    "content":prompt}
    ]
while attempt <= MAX_ATTEMPT:
    try:
        request = {
        "model":model,
        "messages":message,
        }   
        response = httpx.post(url=URL,headers=headers,json=request,timeout=30).json()
        result = response["choices"][0]["message"]["content"]
        output = Employee.model_validate_json(result)
        print(output)
        break
    except ValidationError as e:
        except_message = {"role":"user","content":validate_json(e)}
        message.append(except_message)
        attempt += 1
