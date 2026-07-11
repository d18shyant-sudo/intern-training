from engine.database import sessionLocal,Base
from sqlalchemy import Column,String,Integer,UUID,Boolean,DateTime,DATE
from datetime import datetime
import uuid
class Detail(Base):
    __tablename__ = "details"
    id  = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    name = Column(String)
    email = Column(String,unique=True)
    DOB = Column(DATE)
    created_by = Column(UUID(as_uuid=True),default=uuid.uuid4)
    created_at = Column(DateTime,default=datetime.utcnow())
    updated_by = Column(String,default=None)
    updated_at = Column(DateTime,default=None)
    is_active = Column(Boolean,default=True)
    is_delete = Column(Boolean,default=False)