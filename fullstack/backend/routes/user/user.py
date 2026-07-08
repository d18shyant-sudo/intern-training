from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from engine.database import get_db
from schema.user import Create_detail, detail_response
from service.user import post_detail, get_detail
router = APIRouter(
    prefix="/api/v1",
    tags=["User"]
)
@router.post("/postdetail", response_model=detail_response)
def posts_detail(
    detail: Create_detail,
    db: Session = Depends(get_db)
):
    response = post_detail(detail, db)
    return response
@router.get("/getdetail", response_model=list[detail_response])
def gets_detail(
    db: Session = Depends(get_db)
):
    response = get_detail(db)
    return response