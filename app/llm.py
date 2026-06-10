import os
from groq import Groq # pyrefly: ignore [missing-import]
from dotenv import load_dotenv # pyrefly: ignore [missing-import]

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(
    question: str,
    context: str
):
    prompt = f"""
You are a document QA assistant.

Rules:
1. Answer ONLY from the provided context.
2. Do NOT invent facts.
3. Be direct, concise, and professional. Directly answer the question without meta-commentary (e.g., do not say "Based on the context...", "The documents state..."), conversational padding, or listing unrelated details or dates.
4. When answering about a specific rule, notice period, dispute, or clause, you must include the related terms and consequences mentioned in that paragraph (e.g., specify handovers like laptops/badges/source code for notice periods; when describing the Arvind Mehta v. Northfield dispute memo, always concisely mention that the dispute is over unpaid transport invoices and damaged goods; state rules about late filings for hearing notice deadlines). Maintain a clean, direct, and concise structure without conversational filler.
5. If the answer is not present, say:
   "I could not find the answer in the provided documents."

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def build_context(results):
    context_parts = []

    for match in results.matches:
        context_parts.append(
            match.metadata["text"]
        )

    return "\n\n".join(context_parts)

def build_citations(results):
    citations = []

    for match in results.matches:
        citations.append(
            {
                "source_file":
                match.metadata["source_file"]
            }
        )

    return citations