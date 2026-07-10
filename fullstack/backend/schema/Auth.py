from pydantic import BaseModel
from datetime import datetime
class sign_in(BaseModel):
    username:str
    password:str
class sign_up(BaseModel):
    username:str
    password:str
class token(BaseModel):
    access_token:str
    token_type:str
    expire_at: datetime
