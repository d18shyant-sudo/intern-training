from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
class TaskCreate(BaseModel):
    title:str
    description:str
    completed:bool = False
class TaskResponse(BaseModel):
    id:UUID
    title:str
    description:str
    completed:bool 
    created_at:datetime
    model_config = {
    "from_attributes":True
}