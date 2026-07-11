import os 
from dotenv import load_dotenv
import bcrypt
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from engine.database import get_db
from schema.auth import auth
from service.auth import auth
from fastapi.responses import JSONResponse
load_dotenv()
router = APIRouter(
    prefix="/api/v1",
    tags=["login"]
)
class service:
    @staticmethod
    def encrypt(password:str):
        password_bytes = password.encode("utf-8")
        salt = os.getenv("salt")
        hashed = bcrypt.hashpw(password_bytes,salt)
        return hashed.decode()
    @router.post("/login",response_model=auth.token)
    def user_sign_in(credential:auth.sign_in,db:Session=Depends(get_db)):
        response = auth.sign_in_db(credential,db)
        if isinstance(response,auth.token):
            return response
        if not response:
            return JSONResponse(status_code=400,content="Invalid Credentials")
        return JSONResponse(status_code=500,content={"Error":"Internal Server Error"})
    @router.post("/sign_up",response_model=auth.token)
    def user_sign_up(credential:auth.sign_up,db:Session=Depends(get_db)):
        response = auth.sign_up_in_db(credential,db)
        if isinstance(response,auth.token):
          return response
        if not response :
          return JSONResponse(status_code=400,content="Account already exists Try with new credentials")
        return JSONResponse(status_code=400,content={"Error":"Invalid Attempt.Try Again with new credentials"})