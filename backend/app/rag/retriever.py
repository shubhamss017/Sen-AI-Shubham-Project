import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    "knowledge_base"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve_context(
    query: str,
    top_k: int = 3
):

    embedding = model.encode(
        query,
        normalize_embeddings=True
    ).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    docs = results["documents"][0]

    return "\n\n".join(docs)