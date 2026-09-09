from sqlalchemy.orm import Session
from model import Expense_Policy
import logging
logging.basicConfig(level=logging.INFO)
THRESHOLD = 0.5
class Repository:
    def rag_search(db:Session,query_embedding,k):
        try:
            logging.info("entered repository layer")
            result = db.query(Expense_Policy).filter(Expense_Policy.embedding.cosine_distance(query_embedding)<=THRESHOLD).limit(k).all()
            logging.info(f"no problem in repository {result}")
            return result      
        except Exception as e:
            logging.info(f"The error is {e}")
            return e
            