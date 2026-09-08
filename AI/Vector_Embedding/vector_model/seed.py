from chunk import structure_chunk,header,page_count
from database import session_local
from model import Structure_Chunk
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
db = session_local()
try:
    for key in structure_chunk[header].keys():
     for line in structure_chunk[header][key]:
        if line not in page_count:
            text = line.strip()
            current_chunk  = Structure_Chunk(header=header,sub_heading=key,chunk=line,embeddings=model.encode(text).tolist())
            db.add(current_chunk)
except Exception as e:
    db.rollback()
    print(e)
finally:
    db.commit()

