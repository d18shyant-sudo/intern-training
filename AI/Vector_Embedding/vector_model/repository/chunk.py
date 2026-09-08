from sqlalchemy.orm import Session
from model import Structure_Chunk,Recursive_Chunk,Fixed_Chunk
import logging
logging.basicConfig(level=logging.INFO)
class Repository:
    def fixed_chunk_search(db:Session,query_embedding,k):
        try:
            result = db.query(Fixed_Chunk).order_by(Fixed_Chunk.embeddings.cosine_distance(query_embedding)).limit(k).all()
            logging.info(f"no problem in repository {result}")
            return result      
        except Exception as e:
            return e
    def structure_chunk_search(db:Session,query_embedding,k):
        try:
            result = db.query(Structure_Chunk).order_by(Structure_Chunk.embeddings.cosine_distance(query_embedding)).limit(k).all()
            logging.info(f"no problem in repository {result}")
            return result
        except Exception as e:
            return e
    def recursive_chunk_search(db:Session,query_embedding,k):
        try:
            result = db.query(Recursive_Chunk).order_by(Recursive_Chunk.embeddings.cosine_distance(query_embedding)).limit(k).all()
            logging.info(f"no problem in repository {result}")
            return result
        except Exception as e:
            return e