from pydantic import BaseModel,EmailStr,Field
from datetime import datetime,date
from decimal import Decimal
from enum import Enum
class Employee_Status(str,Enum):
    ACTIVE = "active"
    LEAVE = "on_leave"
    TERMINATED = "terminated"
class Employee(BaseModel):
    name:str
    age:int
    department:str
    role:str
    email:EmailStr
    Date_Of_Join:date
    Date_Of_Birth:date
    Date_Of_Termination:date |None=None
    status : Employee_Status
    salary:Decimal |None = None
    nationality:str |None = None
    address:str |None = None
    pincode:str | None = Field(default=None,pattern=r"^[1-9][0-9]{5}$") 
    