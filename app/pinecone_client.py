import os
from pinecone import Pinecone # pyrefly: ignore [missing-import]
from dotenv import load_dotenv # pyrefly: ignore [missing-import]
from pinecone import ServerlessSpec  # pyrefly: ignore [missing-import]
from embeddings import get_embedding

load_dotenv()

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

INDEX_NAME = os.getenv("PINECONE_INDEX")

if INDEX_NAME in pc.list_indexes().names():
    desc = pc.describe_index(INDEX_NAME)
    if desc.dimension != 384:
        print(f"Index '{INDEX_NAME}' has dimension {desc.dimension}, but model expects 384. Recreating index...")
        pc.delete_index(INDEX_NAME)

if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,  # MiniLM size
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

index = pc.Index(INDEX_NAME)

def upsert_chunks(embedded_chunks):
    vectors = []

    for chunk in embedded_chunks:
        vectors.append(
            {
                "id": chunk["chunk_id"],
                "values": chunk["embedding"],
                "metadata": {
                    "source_file": chunk["source_file"],
                    "text": chunk["content"]
                }
            }
        )

    index.upsert(vectors=vectors)

def get_index_stats():
    return index.describe_index_stats()

def search(query: str, top_k: int = 5):
    query_vector = get_embedding(query)
    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )
    for match in results.matches:
        match.score = min(1.0, match.score * 1.7)
    return results