from repository.chunk import Repository
from utils.embedding import embedder
from sqlalchemy.orm import Session
from schema.chunk import Query
import logging
k = 5
logging.basicConfig(level=logging.INFO)
class Service:
    def rag_search(prompt_query:Query,db:Session,k=k):
        logging.info(f"The query text :{prompt_query.query}")
        query_embedding = embedder(prompt_query.query)
        logging.info(f"The Embeddings of Query :{query_embedding}")
        result = Repository.rag_search(db,query_embedding,k)
        return result

    