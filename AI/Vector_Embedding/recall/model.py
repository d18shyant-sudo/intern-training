from database import Base
from sqlalchemy import Column,Text,UUID,String,Integer
import uuid
from pgvector.sqlalchemy import Vector
class Fixed_Chunk(Base):
    __tablename__="fixed_chunk"
    id = Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    chunk = Column(Text,nullable=False)
    embeddings = Column(Vector(384))
    chunk_id = Column(Integer)
class Recursive_Chunk(Base):
    __tablename__="recursive_chunk"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    chunk = Column(Text,nullable=False)
    embeddings = Column(Vector(384))
    chunk_id = Column(Integer)
class Structure_Chunk(Base):
    __tablename__="structure_chunk"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    header = Column(String,nullable=False)
    sub_heading = Column(String,nullable=False)
    chunk = Column(Text,nullable=False)
    embeddings = Column(Vector(384))
    chunk_id = Column(Integer)
