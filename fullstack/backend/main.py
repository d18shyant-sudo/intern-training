from sqlalchemy.orm import Session
from schema import detail_response,Create_detail
import events
from dependencies import get_db
import CRUD
from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],   # allow GET, POST, PUT, DELETE
    allow_headers=["*"],   # allow all headers
)
@app.post("/api/v1/postdetail")
def post_detail(detail:Create_detail,db:Session=Depends(get_db),response_model=detail_response):
    response = CRUD.create_detail(db,detail)
    return response