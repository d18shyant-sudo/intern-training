from fastapi import Depends
from sqlalchemy.orm import Session
from engine.database import get_db
from schema.user import Create_detail,detail_response
from database.user import create_detail,show_detail
def post_detail(detail:Create_detail,db:Session=Depends(get_db)):
    response = create_detail(detail,db)
    return response
def get_detail(db:Session=Depends(get_db)):
    response = show_detail(db)
    return response