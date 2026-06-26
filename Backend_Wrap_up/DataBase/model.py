from sqlalchemy import Column,Integer,Text,String,Boolean,UUID,DateTime,event
from database import Base
from datetime import datetime
import uuid
class Task(Base):
    __tablename__="tasks"
    id = Column(UUID(as_uuid=True),primary_key=True,default = uuid.uuid4)
    title = Column(String)
    description = Column(Text)
    completed = Column(Boolean)
    created_at = Column(DateTime,default=datetime.utcnow())
    created_by = Column(UUID(as_uuid=True),default=uuid.uuid4)
    updated_by = Column(String,default=None)
    updated_at = Column(DateTime,default=None)
    is_active = Column(Boolean,default=True)
    is_delete = Column(Boolean,default=False)