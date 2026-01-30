from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class ChatRequest(BaseModel):
    session_id: str
    message: str
    temperature: float = 0.2
    model: str = "gpt-4o-mini"

class ChatResponse(BaseModel):
    reply: str
    memory: List[Dict[str, str]]
    logs: List[Dict[str, Any]]
