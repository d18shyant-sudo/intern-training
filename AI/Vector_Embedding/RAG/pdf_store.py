import pymupdf
import os
from dotenv import load_dotenv
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_postgres import PGEngine,PGVectorStore
load_dotenv()

# --------------------------------------------------
# 1. PDF
# --------------------------------------------------

PDF_FILE = "expense_policy.pdf"


# --------------------------------------------------
# 2. Read PDF
# --------------------------------------------------

pdf = pymupdf.open(PDF_FILE)


# --------------------------------------------------
# 3. Markdown structure-aware splitter
# --------------------------------------------------

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "title"),
        ("##", "section"),
        ("###", "subsection"),
    ]
)


documents = []


# --------------------------------------------------
# 4. Split each PDF page
# --------------------------------------------------

for page_number, page in enumerate(pdf, start=1):

    text = page.get_text()

    page_chunks = markdown_splitter.split_text(text)

    for chunk in page_chunks:

        # Citation metadata
        chunk.metadata["document_name"] = PDF_FILE
        chunk.metadata["page"] = page_number

        documents.append(chunk)


pdf.close()


# --------------------------------------------------
# 5. Assign chunk IDs
# --------------------------------------------------

for i, doc in enumerate(documents, start=1):

    doc.metadata["chunk_id"] = i


# --------------------------------------------------
# 6. Create embedding model
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# --------------------------------------------------
# 7. PostgreSQL connection
# --------------------------------------------------

connection = (
    os.getenv("ASYNC_DATABASE_URL")
)


# --------------------------------------------------
# 8. Create LangChain PGVector store
# --------------------------------------------------
pg_engine = PGEngine.from_connection_string(url=connection)
pg_engine.init_vectorstore_table(table_name="expense_policy",vector_size=384)
vector_store = PGVectorStore.create_sync(engine=pg_engine,table_name="expense_policy",embedding_service=embeddings)


# --------------------------------------------------
# 9. Store documents
# --------------------------------------------------

vector_store.add_documents(documents)


print(f"Stored {len(documents)} chunks successfully.")