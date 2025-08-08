"""
Entry point for app. Includes application initialization, 
middleware (if needed), and router inclusion.
"""


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chat

app = FastAPI()

# CORS middleware to allow frontend to call backend APIs
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount all routes in chat.py
app.include_router(chat.router)
