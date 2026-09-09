from database import Base
from sqlalchemy import Column,Text,UUID,String
from sqlalchemy.dialects.postgresql import JSONB
from pgvector.sqlalchemy import Vector
class Expense_Policy(Base):
    __tablename__="expense_policy"
    langchain_id = Column(UUID(as_uuid=True),primary_key=True)
    content = Column(Text,nullable=False)
    embedding = Column(Vector(384))
    langchain_metadata = Column(JSONB)

