from routes.conversation import router as conversation_router
from fastapi import APIRouter
apirouter = APIRouter()
apirouter.include_router(conversation_router)