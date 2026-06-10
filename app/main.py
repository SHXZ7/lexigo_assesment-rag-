import sys
from pathlib import Path

# Add parent directory to sys.path to resolve internal modules correctly
sys.path.append(str(Path(__file__).parent))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from typing import List, Dict, Any
from graph import graph

app = FastAPI(
    title="Legixo Legal RAG API",
    description="API for querying legal documents from the Legixo sample corpus using LangGraph and Pinecone."
)

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    citations: List[Dict[str, Any]]

@app.post("/query", response_model=QueryResponse)
async def query_endpoint(payload: QueryRequest):
    try:
        # Invoke the LangGraph workflow
        result = graph.invoke({
            "question": payload.question
        })
        return {
            "answer": result.get("answer"),
            "citations": result.get("citations", [])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
