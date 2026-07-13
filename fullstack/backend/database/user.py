from sqlalchemy.orm import Session
from schema.user.user import Create_detail
from model.user.user import Detail
from fastapi import Depends
from engine.database import get_db
from fastapi.responses import JSONResponse
from datetime import datetime
def create_detail(detail:Create_detail,db:Session = Depends(get_db)):
    try:
        detail_in_db = db.query(Detail).filter(Detail.email==detail.email).first()
        if detail_in_db:
           return True
        new_detail = Detail(name=detail.name,DOB=detail.dob,email=detail.email)
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
        all_details = db.query(Detail).filter(Detail.is_delete==False).all()
        if not all_details:
            return False
        if isinstance(all_details,list):
            return all_details
    except Exception as e:
        return str(e)
def delete_detail(email:str,db:Session = Depends(get_db)):
    try:
        detail_in_db = (
            db.query(Detail)
            .filter(
                Detail.email == email,
                Detail.is_delete == False
            )
            .first()
        )
        if not detail_in_db:
            return False
        detail_in_db.is_delete = True
        db.commit()
        db.refresh(detail_in_db)
        return detail_in_db
    except Exception as e:
       return str(e)
def update_detail(email: str,detail: Create_detail,db: Session = Depends(get_db)):
    try:
        detail_in_db = (
            db.query(Detail)
            .filter(
                Detail.email == email,
                Detail.is_delete == False
            )
            .first()
        )
        if not detail_in_db:
            return False
        detail_in_db.name = detail.name
        detail_in_db.email = detail.email
        detail_in_db.DOB = detail.dob
        detail_in_db.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(detail_in_db)
        return detail_in_db
    except Exception as e:
        return str(e)
    