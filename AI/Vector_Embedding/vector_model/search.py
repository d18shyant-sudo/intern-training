from database import session_local
from sentence_transformers import SentenceTransformer
from model import Fixed_Chunk,Recursive_Chunk,Structure_Chunk
model = SentenceTransformer("all-MiniLM-L6-v2")
db = session_local()
prompt = input(">>>")
query_embedding = model.encode(prompt)
def k_search(k):
    fixed_chunk_result =  (db.query(Fixed_Chunk).order_by(Fixed_Chunk.embeddings.cosine_distance(query_embedding)).limit(k).all())
    recursive_chunk_result = (db.query(Recursive_Chunk).order_by(Recursive_Chunk.embeddings.cosine_distance(query_embedding)).limit(k).all())
    Structure_chunk_result = (db.query(Structure_Chunk).order_by(Structure_Chunk.embeddings.cosine_distance(query_embedding)).limit(k).all())
    for result in fixed_chunk_result:
        print("\nFixed Chunk Result: ",result.chunk)
    for result in recursive_chunk_result:
        print("\nRecursive Chunk Result: ",result.chunk)
    for result in Structure_chunk_result:
        print("\nStructure Chunk Result:",result.chunk)
k_search(5)