"""
Centralize all data models (schemas) for: 
Request bodies, response models, shared validation logic 
"""

from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

class SaveItem(BaseModel):
    question: str
    answer: str