import chromadb
from sentence_transformers import SentenceTransformer

# =====================================================
# Configuration
# =====================================================

DB_PATH = "./chroma_db"
COLLECTION_NAME = "expense_policy"
POLICY_FILE = "policy.txt"

# =====================================================
# Load Embedding Model
# =====================================================

print("Loading embedding model...")

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# =====================================================
# Connect to ChromaDB
# =====================================================

client = chromadb.PersistentClient(
    path=DB_PATH
)

# Delete the old collection if it exists
try:
    client.delete_collection(COLLECTION_NAME)
except Exception:
    pass

collection = client.create_collection(
    name=COLLECTION_NAME
)

# =====================================================
# Read Policy Document
# =====================================================

with open(POLICY_FILE, "r", encoding="utf-8") as file:
    policy = file.read()

# =====================================================
# Simple Chunking
# =====================================================

chunks = [
    chunk.strip()
    for chunk in policy.split("\n\n")
    if chunk.strip()
]

print(f"Found {len(chunks)} chunks.")

# =====================================================
# Create Embeddings
# =====================================================

embeddings = embedding_model.encode(
    chunks,
    convert_to_numpy=False
)

# =====================================================
# Store in ChromaDB
# =====================================================

for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

    collection.add(
        ids=[str(index)],
        documents=[chunk],
        embeddings=[embedding.tolist()],
        metadatas=[
            {
                "source": POLICY_FILE,
                "chunk": index
            }
        ]
    )

print("\nVector Database Created Successfully!")
print(f"Collection : {COLLECTION_NAME}")
print(f"Chunks     : {len(chunks)}")
print(f"Location   : {DB_PATH}")