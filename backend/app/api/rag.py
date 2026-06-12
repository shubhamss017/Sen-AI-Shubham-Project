import chromadb

from fastapi import APIRouter, Query
from sentence_transformers import SentenceTransformer

router = APIRouter(tags=["RAG"])

# Load once at startup
client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="knowledge_base"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

@router.get("/rag/search")
def search_knowledge(query: str):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1,
        include=["documents", "metadatas", "distances"]
    )

    return {
        "query": query,
        "source": results["metadatas"][0][0]["source"],
        "distance": results["distances"][0][0],
        "content": results["documents"][0][0]
    }