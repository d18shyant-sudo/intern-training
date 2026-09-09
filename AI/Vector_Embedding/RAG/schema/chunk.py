from pydantic import BaseModel
class Query(BaseModel):
    query:str
class Citation(BaseModel):
    document_name:str
    page_no:int
class Query_Response(BaseModel):
    chunk:str
    citations:list[Citation]
    