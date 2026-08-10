from pydantic import BaseModel,ConfigDict
from uuid import UUID
class message(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    id : UUID
    role:str
    content:str
    token:int