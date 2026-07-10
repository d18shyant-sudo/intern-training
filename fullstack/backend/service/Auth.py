from fastapi import Depends
from sqlalchemy.orm import Session
from engine.database import get_db
from schema.Auth import sign_in,sign_up
from database.Auth import Store_login,Sign_in
from service.token.token import create_access_token
from fastapi.responses import JSONResponse
def sign_up_in_db(credential:sign_up,db:Session=Depends(get_db)):
    response = Store_login(credential,db)
    if response.status_code ==200 :
      token = create_access_token(credential.username,credential.password)
      return token
    elif response.status_code== 400:
       return response
    return response
def sign_in_db(credential:sign_in,db:Session=Depends(get_db)):
    response = Sign_in(credential,db)
    if response.status_code == 200:
       token = create_access_token(credential.username,credential.password)
       return token
    elif response.status_code == 400:
       return response
    return response
    

