"""

Defines routes related to chat interactions, save/review functionality,
and speed mode for the Late app. Mounted in main.py.
"""


from fastapi import APIRouter, HTTPException
from app.schemas.schemas import ChatRequest, ChatResponse, SaveItem
from app.services.model_router import get_model
from app.utils.persistence import load_data, save_data
from typing import List

router = APIRouter()

SAVE_FILE = "saved.json"

@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    try:
        model = get_model()
        reply = model.chat(req.message)
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/chat/speed", response_model=ChatResponse)
async def chat_speed(req: ChatRequest):
    try:
        model = get_model(speed_mode=True)
        reply = model.chat(req.message, max_tokens=100)
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/save")
async def save_qa(item: SaveItem):
    data = load_data(SAVE_FILE)

    if item.dict() not in data:
        data.append(item.dict())
        save_data(SAVE_FILE, data)
        return {"status": "saved"}
    else:
        return {"status": "duplicate", "message": "Item already saved."}


@router.get("/review", response_model=List[SaveItem])
async def review_qas():
    return load_data(SAVE_FILE)
