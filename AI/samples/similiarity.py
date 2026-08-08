from sentence_transformers import SentenceTransformer
import chromadb 
model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.create_collection("docs")
docs = [
    "Python is a programming language.",
    "Machine learning uses data.",
    "Cats are pets."
]
for i,doc in enumerate(docs):
    embedding = model.encode(doc).tolist()
    collection.add(ids=[str(i)],embeddings=[embedding],documents=[doc])
query = "Tell me about coding"
query_embedding = model.encode(query).tolist()
results = collection.query(query_embeddings=[query_embedding],n_results=1)
print(results)