from typing import TypedDict
from pinecone_client import search # pyrefly: ignore [missing-import]
from llm import generate_answer
# pyrefly: ignore [missing-import]
from langgraph.graph import (
    StateGraph,
    END
)

class GraphState(TypedDict):
    question: str
    documents: list
    answer: str
    citations: list

def retrieve(state: GraphState):
    question = state["question"]

    results = search(question)

    return {
        "documents": results.matches
    }

def grade_documents(state: GraphState):
    docs = state["documents"]

    if not docs:
        return "reject"

    top_score = docs[0].score

    if top_score > 0.5:
        return "answer"

    return "reject"

def answer(state: GraphState):
    docs = state["documents"]

    context = "\n\n".join(
        doc.metadata["text"]
        for doc in docs
    )

    answer_text = generate_answer(
        state["question"],
        context
    )

    citations = []

    for doc in docs:
        citations.append({
            "source_file":
            doc.metadata["source_file"]
        })

    return {
        "answer": answer_text,
        "citations": citations
    }

def reject(state: GraphState):
    return {
        "answer":
        "I could not find the answer in the provided documents.",
        "citations": []
    }

workflow = StateGraph(
    GraphState
)

workflow.add_node(
    "retrieve",
    retrieve
)

workflow.add_node(
    "answer",
    answer
)

workflow.add_node(
    "reject",
    reject
)

workflow.set_entry_point(
    "retrieve"
)

workflow.add_conditional_edges(
    "retrieve",
    grade_documents,
    {
        "answer": "answer",
        "reject": "reject"
    }
)

workflow.add_edge(
    "answer",
    END
)

workflow.add_edge(
    "reject",
    END
)

graph = workflow.compile()