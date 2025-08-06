"""
Main FastAPI app for Late v1.0 
Handles: 
- AI chat endpoint via OpenAI
- Save/Review Q&A functionality via local JSON
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import openai
import json
import os
from dotenv import load_dotenv

 # Load .env for OpenAI key
load_dotenv() 

app = FastAPI()

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Path to save data
SAVE_FILE = "saved.json"

# ----------------- Models -----------------

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


class SaveItem(BaseModel):
    question: str
    answer: str
    
# ----------------- Routes -----------------

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": req.message}]
        )
        reply = response["choices"][0]["message"]["content"]
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/save")
async def save_qa(item: SaveItem):
    # Load existing data
    try:
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
        else:
            data = []
    except Exception:
        data = []

    # Add new item
    data.append(item.dict())

    # Save back to file
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return {"status": "saved"}


@app.get("/review", response_model=List[SaveItem])
async def review_qas():
    if not os.path.exists(SAVE_FILE):
        return []
    with open(SAVE_FILE, "r") as f:
        data = json.load(f)
    return data