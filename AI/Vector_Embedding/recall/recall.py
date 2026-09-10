import json
from model import Fixed_Chunk,Recursive_Chunk,Structure_Chunk
from database import session_local
from sentence_transformers import SentenceTransformer
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
data_model = {Fixed_Chunk:"fixed_chunk_id",Recursive_Chunk:"recursive_chunk_id",Structure_Chunk:"structure_chunk_id"}
db = session_local()
with open("question.json","r") as file:
    questions= json.load(file)
def recall(k):
    for model,chunk_id in data_model.items():
        total_recall_match_count = 0
        total_question_count =0 
        for i,question in enumerate(questions):
            question_embedding =  embed_model.encode(question[str(i+1)])
            results = db.query(model).order_by(model.embeddings.cosine_distance(question_embedding)).limit(k).all()
            chunk_results = [result.chunk_id for result in results]
            if any (x in chunk_results for x in question[chunk_id]):
                total_recall_match_count += 1
            total_question_count += 1
        print(f"recall@{k} for {str(model.__name__)} is {(total_recall_match_count/total_question_count)*100}%")
    db.close()
recall(3)
recall(5)




