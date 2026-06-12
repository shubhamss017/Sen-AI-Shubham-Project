from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

KB_PATH = Path("D:\sen ai 2\knowledge_base")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="knowledge_base"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

documents = []

for file in KB_PATH.glob("*.md"):

    text = file.read_text(
        encoding="utf-8"
    )

    documents.append(
        {
            "id": file.stem,
            "text": text,
            "source": file.name
        }
    )

for doc in documents:

    embedding = model.encode(
        doc["text"]
    ).tolist()

    collection.add(
        ids=[doc["id"]],
        documents=[doc["text"]],
        embeddings=[embedding],
        metadatas=[
            {
                "source": doc["source"]
            }
        ]
    )

print(
    f"Ingested {len(documents)} documents"
)