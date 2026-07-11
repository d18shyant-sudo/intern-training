from engine.database import Base,sessionLocal
from sqlalchemy import Column,String
class Login(Base):
    __tablename__="login"
    username = Column(String)
    password = Column(String,primary_key=True)

