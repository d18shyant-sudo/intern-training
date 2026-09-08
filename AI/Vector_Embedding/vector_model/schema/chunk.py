from pydantic import BaseModel
class Query(BaseModel):
    query:str
class Query_Response(BaseModel):
    chunk:str