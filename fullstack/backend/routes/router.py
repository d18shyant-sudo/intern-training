from fastapi import APIRouter
from routes.user.user import router as user_router
api_router = APIRouter()
api_router.include_router(user_router)