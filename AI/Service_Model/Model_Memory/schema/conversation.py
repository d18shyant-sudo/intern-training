from pydantic import BaseModel
from uuid import UUID
from typing import Text
from datetime import datetime
class ConversationRequest(BaseModel):
    req_id:UUID
    user_id:UUID
    model_name:str
    prompt:Text
    response:Text
    created_by:UUID
    created_at: datetime 
class ConversationResponse(BaseModel):
    req_id:str
    user_id:str
    model_name:str
    prompt:Text
    response:Text
class ConversationHistory(BaseModel):
    id:UUID
