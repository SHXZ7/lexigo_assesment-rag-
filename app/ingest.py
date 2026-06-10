from dataclasses import dataclass
from pathlib import Path
# pyrefly: ignore [missing-import]
from langchain_text_splitters import RecursiveCharacterTextSplitter
from embeddings import get_embedding
from pinecone_client import upsert_chunks, get_index_stats

@dataclass
class Document:
    file_name: str
    content: str
    chunk_id: str = ""

    @property
    def source_file(self) -> str:
        return self.file_name

def embed_chunks(chunks):
    embedded_chunks = []

    for chunk in chunks:
        embedded_chunks.append(
            {
                "chunk_id": chunk.chunk_id,
                "source_file": chunk.source_file,
                "content": chunk.content,
                "embedding": get_embedding(
                    chunk.content
                )
            }
        )

    return embedded_chunks

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )

    chunks = []

    for doc in documents:
        split_texts = splitter.split_text(doc.content)
        for idx, text in enumerate(split_texts):
            chunks.append(
                Document(
                    chunk_id=f"{doc.file_name}_chunk_{idx}",
                    file_name=doc.file_name,
                    content=text
                )
            )

    return chunks


    
def load_documents(corpus_path : str):
    documents = []

    path = Path(corpus_path)
    if not path.exists():
        path = Path(__file__).parent / corpus_path

    for file_path in path.glob("*.md"):
        if file_path.name == "testcases.md":
            continue
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        documents.append(
            Document(
                file_name=file_path.name,
                content=content
            )
        )

    return documents

if __name__ == "__main__":
    docs = load_documents("../doc")

    chunks = chunk_documents(docs)

    embedded_chunks = embed_chunks(chunks)

    print(
        f"Created {len(embedded_chunks)} embeddings"
    )

    print(
        "Embedding dimension:",
        len(embedded_chunks[0]["embedding"])
    )

    print("Upserting chunks to Pinecone...")
    upsert_chunks(embedded_chunks)
    print("Upsert successful!")

    print("\nVerifying Pinecone Index Stats:")
    print(get_index_stats())
