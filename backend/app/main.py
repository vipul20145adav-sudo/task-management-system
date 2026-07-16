from fastapi import FastAPI
from app.api.user import router as user_router

app = FastAPI(
    title="AI Powered Task Management System",
    version="1.0.0"
)

app.include_router(user_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Powered Task Management System"
    }
