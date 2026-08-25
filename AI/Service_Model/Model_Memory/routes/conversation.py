from fastapi import APIRouter,Depends
from json import JSONEncoder
import logging
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from schema.conversation import ConversationRequest,ConversationResponse,ConversationHistory
from service.conversation import Service
from engine import get_db
logging.basicConfig(level=logging.INFO)
router = APIRouter(prefix="/api/v1",tags=["Conversation"])
@router.post("/post-conversation")
def post_conversation(request:ConversationRequest,db:Session = Depends(get_db)):
    try:
        result = Service.post_conversation(request,db)
        if result:
            return JSONResponse(status_code=200,content={"Message":"Added Successfully"})
        if not result:
            return JSONResponse(status_code=400,content={"Error":"error in requests"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Internal Server Error":str(e)})
@router.post("/get-conversation",response_model=list[ConversationResponse])
def get_conversation(req_id:ConversationHistory,db:Session = Depends(get_db)):
    try:
        results  = Service.get_conversation(req_id,db)
        if results:
            logging.info([result.id for result in results])
            return JSONResponse(status_code=200,content=[{"req_id":str(result.req_id),"user_id":str(result.user_id),"model_name":result.model_name,"prompt":result.prompt,"response":result.response,} for result in results])
        if not results:
            return JSONResponse(status_code=404,content={"Error":"Resource is not found"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Internal Server Error":str(e)})