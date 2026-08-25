from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schema.Model import Employee,Salary,Employee_response,Salary_response
from tools.tools import get_employee,calculate_bonus
import httpx
import os
import json
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
load_dotenv()
URL = os.getenv("URL")
API = os.getenv("OPEN_ROUTER_API")
headers = {
    "Authorization":f"Bearer {API}",
    "Content-Type":"application/json"
}
messages = {
    "model":"dots-studio/dots-3-note-preview:free",
    "messages":[{"role":"user","content":"what is mean by ai elaborately define that with 10 points"}],
    "stream":True
}
router = APIRouter()
@router.post("/service/get-employee",response_model=Employee_response)
def router_get_employee(emp_id:Employee):
    try :
        result = get_employee(emp_id=emp_id.emp_id)
        if result:
            return JSONResponse(status_code=200,content=result)
        else:
            return JSONResponse(status_code=404,content={"Error":"No such employee"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Internal Server Error"})
@router.post("/service/calculate-salary",response_model=Salary_response)
def router_calculate_salary(salary:Salary):
    try:
        result = calculate_bonus(salary=salary.salary)
        if result:
            return JSONResponse(status_code=200,content={"Calculated bonus for this salary":result})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Internal Server Error"})
@router.get("/service/stream-data")
def stream_data():    
    def generate():
        with httpx.stream("POST",url=URL,headers=headers,json=messages,timeout=30) as response:
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
                if content:
                    yield content
    return StreamingResponse(generate(),media_type="text/plain")
