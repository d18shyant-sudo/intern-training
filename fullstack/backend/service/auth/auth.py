from fastapi import Depends
from sqlalchemy.orm import Session
from engine.database import get_db
from schema.auth.auth import sign_up,sign_in
from database.auth import Store_login,Sign_in
from service.token.token import create_access_token
from fastapi.responses import JSONResponse
def sign_up_in_db(credential:sign_up,db:Session=Depends(get_db)):
    response = Store_login(credential,db)
    if response :
      token = create_access_token(credential.username,credential.password)
      return token
    elif response == False:
       return False
    return response
def sign_in_db(credential:sign_in,db:Session=Depends(get_db)):
    response = Sign_in(credential,db)
    if response:
       token = create_access_token(credential.username,credential.password)
       return token
    elif response == False :
       return False
    return response
    

