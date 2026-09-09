from sentence_transformers import SentenceTransformer
from schema.chunk import Query
import logging
model = SentenceTransformer("all-MiniLM-L6-v2")
logging.basicConfig(level=logging.INFO)
def embedder(query):
    logging.info(f"embedding chunk:{query}")
    logging.info("error in util")
    return model.encode(query)