from model.user.user import Detail
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from engine.database import get_db
from schema.user.user import Create_detail,detail_response
from service.user.user import service
from fastapi.responses import JSONResponse
import logging
logging.basicConfig(level=logging.INFO)
router = APIRouter(
    prefix="/api/v1",
    tags=["User"]
)
@router.post("/postdetail", response_model=detail_response)
def posts_detail(
    detail: Create_detail,
    db: Session = Depends(get_db)
):
    response = service.post_detail(detail, db)
    if  response == True:
        logging.info("it gives null")
        return JSONResponse(status_code=400,content={"Error":"User is already exists"})
    elif isinstance(response,Detail):
        logging.info("it gives value")
        return JSONResponse(status_code=200,content={"name":response.name,"email":response.email,"DOB":str(response.DOB)})
    else:
        logging.info("internal issues")
        return JSONResponse(status_code=500,content={"Error":response})
@router.get("/getdetail", response_model=list[detail_response])
def gets_detail(
    db: Session = Depends(get_db)
):
    response = service.get_detail(db)
    if response == False:
        logging.info("it shows the null")
        return JSONResponse(status_code=400,content={"Error":"No user exits"})
    elif isinstance(response,list):
        return JSONResponse(status_code=200,content=[{"name":user.name,"email":user.email,"DOB":str(user.DOB)} for user in response])
    logging.info("no such conent in db")
    return JSONResponse(status_code=500,content={"Error":response})
@router.delete("/deletedetail/{email}")
def delete_user(
    email:str,
    db:Session = Depends(get_db)
):

    response = service.delete_detail(email,db)
    if response == False:
        logging.info(
            "user does not exist"
        )
        return JSONResponse(
            status_code=404,
            content={
                "Error":"User does not exist"
            }
        )
    elif isinstance(response,Detail):
        logging.info(
            "user soft deleted"
        )
        return JSONResponse(
            status_code=200,
            content={
                "message":
                "User deleted successfully"
            }
        )
    return JSONResponse(
        status_code=500,
        content={
            "Error":response
        }
    )
@router.put("/updatedetail/{email}")
def update_user(
    email:str,
    detail:Create_detail,
    db:Session=Depends(get_db)
):

    response = service.update_detail(
        email,
        detail,
        db
    )


    if response == False:

        return JSONResponse(
            status_code=404,
            content={
                "Error":"User not found"
            }
        )


    elif isinstance(response,Detail):

        return JSONResponse(
            status_code=200,
            content={
                "message":"User updated successfully"
            }
        )


    return JSONResponse(
        status_code=500,
        content={
            "Error":response
        }
    )