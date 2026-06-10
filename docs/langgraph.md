# LangGraph Workflow Documentation

This document describes the structure and behavior of the state machine defined in [app/graph.py](file:///c:/Users/HP/Documents/gen_ai_takehome_sample_corpus/app/graph.py).

---

## State Diagram

```text
START
  ↓
retrieve
  ↓
grade_documents
 /           \
answer      reject
 ↓            ↓
END          END
```

---

## Node Mapping

| Node | Purpose |
| :--- | :--- |
| **retrieve** | Search Pinecone vector database |
| **grade_documents** | Check relevance of retrieved documents (threshold: `0.5`) |
| **answer** | Generate grounded answer from context |
| **reject** | Return no-answer response |

---

## State Variables (`GraphState`)

The state passed between nodes is defined as:
* **`question` (`str`)**: The user's input query.
* **`documents` (`list`)**: The retrieved matching document chunks from Pinecone.
* **`answer` (`str`)**: The generated final text response from the LLM or a fallback rejection statement.
* **`citations` (`list`)**: A list of source file references for the answer.

---

## Loop and Execution Limits
This graph is completely **acyclic (DAG)** and contains no looping paths. As a result:
* **Maximum Path Length**: The maximum execution path is exactly **2 nodes** (`retrieve` followed by either `answer` or `reject`).
* **Loop Safety**: It is structurally impossible for the execution loop to spin infinitely.
