from pydantic import BaseModel,ConfigDict
import json
class Employee(BaseModel):
    model_config =  ConfigDict(validate_assignment=True)
    id:int
    name:str
    department:str
with open("employees.json","r") as file:
    datas = json.load(file)
employees = [Employee(**data) for data in datas ]
# employees[0].id = "hi"
print(employees)
