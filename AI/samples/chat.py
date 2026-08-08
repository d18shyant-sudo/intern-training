import json
import ollama
import chromadb

from sentence_transformers import SentenceTransformer
from pydantic import BaseModel

# =====================================================
# Pydantic Schema
# =====================================================

class ExpenseClaim(BaseModel):
    employee_name: str
    amount: float
    category: str

schema = ExpenseClaim.model_json_schema()

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
    path="./chroma_db"
)

collection = client.get_collection(
    "expense_policy"
)

# =====================================================
# System Prompt
# =====================================================

system_prompt = f"""
You are an AI assistant for an Expense Management System.

Current authenticated user:
- EMP001 (Robert)

You have access to two capabilities.

Capability A:
Extract structured information from user requests that describe an expense-related operation. Produce valid JSON matching the following schema. Do NOT wrap the JSON in Markdown.

Schema:
{json.dumps(schema, indent=2)}

Capability B:
Answer questions using the information provided in the Context section. The Context contains external knowledge that you do not inherently know. Use only the Context when it is relevant.Use the Context as your only source of truth.

If the Context contains enough information to answer the user's question, answer using only that information.

If the Context contains only a partial answer, provide the available information and clearly state that the Context may be incomplete.

Only reply "I couldn't find that information." when the Context contains no relevant information at all.
Instructions:

- First understand the user's intent.
- Decide which capability is appropriate for the current request.
- Use exactly one capability unless the user explicitly asks for multiple tasks.
- If you choose Capability A, return ONLY valid JSON.
- If you choose Capability B, return a natural language answer.
- Do not invent information that is not present in the Context.
- Resolve pronouns such as "I", "me", and "my" as the authenticated user.
- Ask for clarification instead of guessing when required information is missing.
"""

print("Assistant Ready")

# =====================================================
# Chat Loop
# =====================================================

while True:

    user_input = input("\n>>> ")

    if user_input.lower() == "exit":
        break

    # -------------------------------------------------
    # Create query embedding
    # -------------------------------------------------

    query_embedding = embedding_model.encode(
        user_input
    ).tolist()

    # -------------------------------------------------
    # Search ChromaDB
    # -------------------------------------------------

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    documents = results.get("documents", [[]])

    context = ""

    if documents and len(documents[0]) > 0:
        context = "\n\n".join(documents[0])
    print("\n========== Retrieved Context ==========") 
    print(context)
    print("=======================================\n")
    # -------------------------------------------------
    # Build Prompt
    # -------------------------------------------------

    prompt = f"""
Context:

{context}

User Request:

{user_input}
"""

    # -------------------------------------------------
    # Call Ollama
    # -------------------------------------------------

    response = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"].strip()

    # -------------------------------------------------
    # Try JSON
    # -------------------------------------------------

    try:

        obj = json.loads(content)

        print("\nExtracted JSON\n")
        print(json.dumps(obj, indent=4))

    except Exception:

        print("\nAssistant\n")
        print(content)