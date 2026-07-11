from sqlalchemy.orm import Session
from schema.user import user
from model.user import user
from fastapi import Depends
from engine.database import get_db
from fastapi.responses import JSONResponse
def create_detail(detail:user.Create_detail,db:Session = Depends(get_db)):
    try:
        detail_in_db = db.query(user.Detail).filter(user.Detail.email==detail.email).first()
        if detail_in_db:
           return detail_in_db
        new_detail = user.Detail(name=detail.name,DOB=detail.dob,email=detail.email)
        db.add(new_detail)
        db.commit()
        db.refresh(new_detail)
        new_detail.created_by = new_detail.id
        db.commit()
        return new_detail
    except Exception as e:
        return str(e)
def show_detail(db:Session = Depends(get_db)):
    try:
        all_details = db.query(user.Detail).all()
        return all_details
    except Exception as e:
        return str(e)
    