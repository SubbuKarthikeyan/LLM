from app.core.config import settings

MODELS = [
    {
        "name": "Llama",
        "model": "groq/llama-3.1-8b-instant",
        "api_key": settings.GROQ_API_KEY
    },
    {
        "name": "Gemini",
        "model": "gemini/gemini-2.5-flash",
        "api_key": settings.GEMINI_API_KEY
    }
]


