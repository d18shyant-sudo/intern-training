from sqlalchemy.orm import Session
from schema.Auth import sign_in
from model.Auth import Login
from fastapi import Depends
from engine.database import get_db
import logging
from fastapi.responses import JSONResponse
from database.password.encrypt import encrypt
logging.basicConfig(level=logging.info)
def Store_login(credential:sign_in,db:Session = Depends(get_db)):
    try:
        credential_in_db = db.query(Login).filter(Login.password==encrypt(credential.password)).first()
        logging.info("db is reached 1")
        if credential_in_db:
            return JSONResponse(status_code=400,content="Account already exists Try with new credentials")
        new_credential = Login(username=credential.username,password=encrypt(credential.password))
        logging.info("db is reached 2")
        db.add(new_credential)
        logging.info("db is reached 3")
        db.commit()
        logging.info("db is reached 4")
        db.refresh(new_credential)
        logging.info("db is reached 5")
        return JSONResponse(status_code=200,content="Account added successfully")
    except Exception as e:
        logging.info("db is not reached")
        return JSONResponse(status_code=404,content="Invalid Attempt Try Again")
def Sign_in(credential:sign_in,db:Session = Depends(get_db)):
    try:
        password_in_db = db.query(Login).filter(Login.password==encrypt(credential.password)).first()
        username_in_db = db.query(Login).filter(Login.username==credential.username).first()
        if password_in_db and username_in_db:
             return JSONResponse(status_code=200,content="Account added successfully")
        if not password_in_db and username_in_db:
            return JSONResponse(status_code=400,content="Invalid Credentials")
        else:
            return JSONResponse(status_code=404,content="No such account try to sign up")
    except Exception as e:
        return JSONResponse(status_code=500,content={"Error":str(e)})
