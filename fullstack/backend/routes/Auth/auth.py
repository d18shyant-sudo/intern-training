import os 
from dotenv import load_dotenv
import bcrypt
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from engine.database import get_db
from schema.auth.auth import sign_in,sign_up,token
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
        hashed = bcrypt.hashpw(password_bytes,bcrypt.gensalt())
        return hashed.decode("utf-8")
    @router.post("/login",response_model=token)
    def user_sign_in(credential:sign_in,db:Session=Depends(get_db)):
        response = auth.sign_in_db(credential,db)
        if response:
            return response
        elif response == False:
            return JSONResponse(status_code=400,content="Invalid Credentials")
        return JSONResponse(status_code=500,content={"Error":"Internal Server Error"})
    @router.post("/sign_up",response_model=token)
    def user_sign_up(credential:sign_up,db:Session=Depends(get_db)):
        credential.password = service.encrypt(credential.password)
        response = auth.sign_up_in_db(credential,db)
        if response:
          return response
        if response == False :
          return JSONResponse(status_code=400,content="Account already exists Try with new credentials")
        return JSONResponse(status_code=400,content={"Error":"Invalid Attempt.Try Again with new credentials"})