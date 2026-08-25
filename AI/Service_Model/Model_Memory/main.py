from fastapi import FastAPI
from routes.router import apirouter
app = FastAPI()
app.include_router(apirouter)