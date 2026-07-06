from sqlalchemy.orm import Session
from schema import Create_detail
from model import Detail
from fastapi.responses import JSONResponse
def create_detail(db:Session,detail:Create_detail):
    try:
        detail_in_db = db.query(Detail).filter(Detail.email==detail.email).first()
        if detail_in_db:
            return JSONResponse(status_code=400,content={"User is already exists"})
        new_detail = Detail(name=detail.name,DOB=detail.dob,email=detail.email)
        db.add(new_detail)
        db.commit()
        db.refresh(new_detail)
        # new_detail.created_by = new_detail.id
        db.commit()
    except Exception as e:
        return JSONResponse(status_code=400,content={"Error":str(e)})
    