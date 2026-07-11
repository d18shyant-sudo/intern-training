from pydantic import BaseModel,EmailStr
from uuid import UUID
from datetime import date
class Create_detail(BaseModel):
    name:str
    dob:date
    email:EmailStr
class detail_response(BaseModel):
    name:str
    DOB:date
    email:EmailStr
    model_config ={"from_attributes":True}