import os 
from dotenv import load_dotenv
load_dotenv()
class Settings:
    DATABASE_URL=os.getenv("DATABASE_URL","postgresql+psycopg2://postgres:dushy123@localhost:5432/backend")
settings = Settings()