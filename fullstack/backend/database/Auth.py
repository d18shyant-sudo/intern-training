from sqlalchemy.orm import Session
from schema.auth import auth
from model.auth import auth
from fastapi import Depends
from engine.database import get_db
import logging
from fastapi.responses import JSONResponse
def Store_login(credential:auth.sign_in,db:Session = Depends(get_db)):
    try:
        credential_in_db = db.query(auth.Login).filter(auth.Login.password==(credential.password)).first()
        if credential_in_db:
            return []
        new_credential = auth.Login(username=credential.username,password=(credential.password))
        db.add(new_credential)
        db.commit()
        db.refresh(new_credential)
        return new_credential
    except Exception as e:
        return str(e)
def Sign_in(credential:auth.sign_in,db:Session = Depends(get_db)):
    try:
        password_in_db = db.query(auth.Login).filter(auth.Login.password==(credential.password)).first()
        username_in_db = db.query(auth.Login).filter(auth.Login.username==credential.username).first()
        if password_in_db and username_in_db:
             return credential
        else:
            return []
    except Exception as e:
        return str(e)
        
