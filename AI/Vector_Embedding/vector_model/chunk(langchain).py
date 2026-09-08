import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_postgres import PGEngine, PGVectorStore
load_dotenv()
# 1. Load PDF
loader = PyMuPDFLoader(
    "Mountains-Extend.pdf"
)

documents = loader.load()

# 2. Recursive chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
)

chunks = splitter.split_documents(documents)

# 3. Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# 4. PostgreSQL connection
connection = (
    os.getenv("ASYNC_DATABASE_URL")
)

pg_engine = PGEngine.from_connection_string(
    url=connection
)

# 5. Create vector table
pg_engine.init_vectorstore_table(
    table_name="mountain_chunks",
    vector_size=384,
)

# 6. Create vector store
vector_store = PGVectorStore.create_sync(
    engine=pg_engine,
    table_name="mountain_chunks",
    embedding_service=embedding_model,
)

# 7. Store chunks + embeddings
vector_store.add_documents(chunks)

# 8. Search
query = "what is mean by mountain?"

results = vector_store.similarity_search(
    query,
    k=3,
)

# 9. Print only chunk text
for result in results:
    print(result.page_content)
    print("----------------")