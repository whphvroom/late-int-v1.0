"""
Entry point for app. Includes application initialization, 
middleware (if needed), and router inclusion.
"""


from fastapi import FastAPI
from app.routes import chat

app = FastAPI()

# Mount all routes in chat.py
app.include_router(chat.router)
