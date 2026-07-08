import os
import logging
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine
from engine.config import settings
logging.basicConfig(level=logging.INFO)
Base = declarative_base()
load_dotenv()
DATABASE_URL=settings.DATABASE_URL
def test_connection():
    engine = create_engine(DATABASE_URL)
    logging.info("Database connection enabled")
    return engine
sessionLocal= sessionmaker(bind=test_connection())
def get_db():
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()
    