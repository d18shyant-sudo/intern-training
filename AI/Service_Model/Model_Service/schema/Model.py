from pydantic import BaseModel
class Employee(BaseModel):
    emp_id:int
class Salary(BaseModel):
    salary:int
class Employee_response(BaseModel):
    name:str
    age:int
    salary:int
class Salary_response(BaseModel):
    salary:int