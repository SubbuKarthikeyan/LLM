from fastapi import FastAPI
from app.routes import chatbot

app = FastAPI()

@app.get("/")
def landing_page():
    return {
        "message": "hello there !!!"
    }

@app.get("/health")
def health():
    return{
        "message": "your backend is good"
    }

app.include_router(chatbot.router)



