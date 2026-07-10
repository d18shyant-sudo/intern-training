from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from engine.database import get_db
from schema.Auth import token,sign_in,sign_up
from service.Auth import sign_up_in_db,sign_in_db
router = APIRouter(
    prefix="/api/v1",
    tags=["login"]
)
@router.post("/login",response_model=token)
def user_sign_in(credential:sign_in,db:Session=Depends(get_db)):
    response = sign_in_db(credential,db)
    return response
@router.post("/sign_up",response_model=token)
def user_sign_up(credential:sign_up,db:Session=Depends(get_db)):
    response = sign_up_in_db(credential,db)
    return response