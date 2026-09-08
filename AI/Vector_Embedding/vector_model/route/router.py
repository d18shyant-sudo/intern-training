from route.chunk import router as chunk_router
from fastapi import APIRouter
api_router =  APIRouter()
api_router.include_router(chunk_router)