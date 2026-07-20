from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.core.models import MODELS
from app.utils.fallback import fallback_request
from app.prompts.system_prompt import SYSTEM_PROMPT

from app.rag.retriever import Retriever
from app.prompts.rag_prompt import build_rag_prompt

router = APIRouter()

retriever = Retriever()



'''
# -----------------------------
# Normal Chat Response
# -----------------------------
@router.post("/chatbot")
def chatbot(message: str):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": message
        }
    ]

    response = fallback_request(
        models=MODELS,
        messages=messages,
        temperature=1.5,
        max_tokens=100
    )

    return {
        "reply": response["response"].choices[0].message.content,
        "provider": response["provider"],
        "model": response["model"],
        "fallback": response["fallback"]
    }
'''

# -----------------------------
# Streaming Generator
# -----------------------------
def stream_generator(message: str):

    print("=" * 50)
    print("Streaming request received")
    print(f"Message: {message}")

    # Retrieve relevant chunks
    context = retriever.retrieve(message)
    print("=" * 50)
    print("User Question:", message)
    print("=" * 50)

    for i, chunk in enumerate(context, start=1):
        print(f"\nChunk {i}")
        print("-" * 40)
        print(chunk)

    # Build the RAG prompt
    rag_prompt = build_rag_prompt(
        context=context,
        question=message
    )

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": rag_prompt
        }
    ]

    response = fallback_request(
        models=MODELS,
        messages=messages,
        stream=True,
        temperature=0.3,
        max_tokens=500
    )

    for chunk in response:
        if chunk.choices and chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content


# -----------------------------
# Streaming Chat Response
# -----------------------------
@router.post("/chatbot/stream")
def chatbot_stream(message: str):

    return StreamingResponse(
        stream_generator(message),
        media_type="text/plain"
    )


