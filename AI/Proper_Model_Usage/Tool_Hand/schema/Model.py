from pydantic import BaseModel
class Employee(BaseModel):
    emp_id:int
class Salary(BaseModel):
    salary:int
