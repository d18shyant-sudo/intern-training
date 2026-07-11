from datetime import datetime,timedelta
import jwt
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from engine.database import get_db
from schema.user import user 
from service.user import user
from fastapi.responses import JSONResponse
router = APIRouter(
    prefix="/api/v1",
    tags=["User"]
)
@router.post("/postdetail", response_model=user.detail_response)
def posts_detail(
    detail: user.Create_detail,
    db: Session = Depends(get_db)
):
    response = user.post_detail(detail, db)
    if not response:
        return JSONResponse(status_code=400,content={"Error":"User is already exists"})
    elif response:
        return JSONResponse(status_code=200,content=response)
    else:
        return JSONResponse(status_code=500,content={"Error":response})
@router.get("/getdetail", response_model=list[user.detail_response])
def gets_detail(
    db: Session = Depends(get_db)
):
    response = user.get_detail(db)
    if not response:
        return JSONResponse(status_code=400,content={"Error":"No user exits"})
    elif response:
        return JSONResponse(status_code=200,content=response)
    return JSONResponse(status_code=500,content={"Error":response})
