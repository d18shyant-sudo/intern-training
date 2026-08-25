from sqlalchemy import Column,TEXT,UUID,String,DateTime
import uuid
from database import Base
class Conversation(Base):
    __tablename__="conversations"
    id =  Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    req_id = Column(UUID(as_uuid=True),nullable=False)
    user_id = Column(UUID(as_uuid=True),nullable=False)
    model_name = Column(String,nullable=False)
    prompt = Column(TEXT,nullable=False)
    response = Column(TEXT,nullable=False)
    created_at = Column(DateTime,nullable=False)
    updated_at = Column(DateTime)
    created_by = Column(UUID(as_uuid=True),nullable=False)
    updated_by = Column(UUID(as_uuid=True))