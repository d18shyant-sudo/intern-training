from fastapi import APIRouter
from routes.user.user import router as user_router
from routes.Auth.auth import router as login_router
api_router = APIRouter()
api_router.include_router(user_router)
api_router.include_router(login_router)