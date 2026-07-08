from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from engine.database import get_db
app = FastAPI()
from schema.user import Create_detail,detail_response
from service.user import post_detail,get_detail
@app.post("/api/v1/postdetail",response_model=detail_response)
def posts_detail(detail:Create_detail,db:Session=Depends(get_db)):
    response = post_detail(detail,db)
    return response
@app.get("/api/v1/getdetail",response_model=list[detail_response])
def gets_detail(db:Session=Depends(get_db)):
    response = get_detail(db)
    return response