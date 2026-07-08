from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.router import api_router
from engine.database import test_connection
app = FastAPI()
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)