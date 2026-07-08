from routes.user.user import app
from engine.database import test_connection
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],   # allow GET, POST, PUT, DELETE
    allow_headers=["*"],   # allow all headers
)
