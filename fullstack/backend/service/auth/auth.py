from fastapi import Depends
from sqlalchemy.orm import Session
from engine.database import get_db
from schema.auth import auth
from database.auth import auth
from service.token import token
from fastapi.responses import JSONResponse
def sign_up_in_db(credential:auth.sign_up,db:Session=Depends(get_db)):
    response = auth.Store_login(credential,db)
    if response  :
      token = token.create_access_token(credential.username,credential.password)
      return token
    elif not response:
       return response
    return response
def sign_in_db(credential:auth.sign_in,db:Session=Depends(get_db)):
    response = auth.Sign_in(credential,db)
    if response:
       token = token.create_access_token(credential.username,credential.password)
       return token
    elif not response :
       return response
    return response
    

