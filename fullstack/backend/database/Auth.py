from sqlalchemy.orm import Session
from schema.auth.auth import sign_in,sign_up
from model.auth.auth import Login
from fastapi import Depends
from engine.database import get_db
import logging
from fastapi.responses import JSONResponse
def Store_login(credential: sign_up, db: Session = Depends(get_db)):
    try:
        credential_in_db = db.query(Login).filter(
            Login.username == credential.username
        ).first()
        if credential_in_db:
            return False
        new_credential = Login(
            username=credential.username,
            password=credential.password
        )
        db.add(new_credential)
        db.commit()
        db.refresh(new_credential)
        return new_credential
    except Exception as e:
        return str(e)
def Sign_in(credential:sign_in,db:Session = Depends(get_db)):
    try:
        username_in_db = db.query(Login).filter(Login.username==credential.username).first()
        if username_in_db:
             return credential
        else:
            return False
    except Exception as e:
        return str(e)
        
