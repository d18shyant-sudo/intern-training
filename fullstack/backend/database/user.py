from sqlalchemy.orm import Session
from schema.user import Create_detail
from model.user import Detail
from fastapi import Depends
from engine.database import get_db
from fastapi.responses import JSONResponse
def create_detail(detail:Create_detail,db:Session = Depends(get_db)):
    try:
        detail_in_db = db.query(Detail).filter(Detail.email==detail.email).first()
        if detail_in_db:
            return JSONResponse(status_code=400,content={"Error":"User is already exists"})
        new_detail = Detail(name=detail.name,DOB=detail.dob,email=detail.email)
        db.add(new_detail)
        db.commit()
        db.refresh(new_detail)
        new_detail.created_by = new_detail.id
        db.commit()
        return new_detail
    except Exception as e:
        return JSONResponse(status_code=400,content={"Error":str(e)})
def show_detail(db:Session = Depends(get_db)):
    try:
        all_details = db.query(Detail).all()
        if not all_details :
            return JSONResponse(status_code=400,content={"Error":"No user exits"})
        return all_details
    except Exception as e:
        return JSONResponse(status_code=400,content={"Error":str(e)})
    