from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chatbot

app = FastAPI(title="Trase Bus Travel API", version="1.0.0")

# Allow the React dev server (and any origin in dev) to call the API.
# Restrict origins to your deployed frontend URL in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def landing_page():
    return {"message": "Trase Bus Travel API — use POST /chatbot/stream to chat."}


@app.get("/health")
def health():
    return {"status": "ok", "message": "Backend is healthy."}


app.include_router(chatbot.router)



