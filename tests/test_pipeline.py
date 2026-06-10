import sys
from pathlib import Path

# Add the app directory to sys.path so we can import modules from it
sys.path.append(str(Path(__file__).parent / "app"))

# pyrefly: ignore [missing-import]
from pinecone_client import search  
from llm import build_context, generate_answer, build_citations # pyrefly: ignore [missing-import]

if __name__ == "__main__":
    query = "When is the hearing scheduled?"
    print(f"Query: {query}\n")

    print("Searching Pinecone...")
    results = search(query, top_k=5)
    for idx, match in enumerate(results.matches):
        print(f"  [{idx}] Score: {match.score:.4f} | Source: {match.metadata.get('source_file')}")
        print(f"      Text excerpt: {match.metadata.get('text')[:100]}...")

    print("\nBuilding context...")
    context = build_context(results)

    print("\nGenerating answer from Groq LLM...")
    try:
        answer = generate_answer(
            question=query,
            context=context
        )
        citations = build_citations(results)

        output = {
            "answer": answer,
            "citations": citations
        }

        import json
        print("\nPipeline Response:")
        print(json.dumps(output, indent=2))
    except Exception as e:
        print(f"\n[Error during LLM generation]: {e}")
        print("\nMake sure GROQ_API_KEY is correctly set in your .env file or environment.")
