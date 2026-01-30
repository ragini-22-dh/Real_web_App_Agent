from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

from models import ChatRequest, ChatResponse
from memory import get_memory, add_message, get_logs, add_log, reset_session
from agent import run_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    mem = get_memory(req.session_id)

    add_log(req.session_id, {
        "ts": datetime.utcnow().isoformat(),
        "type": "request",
        "message": req.message,
        "model": req.model,
        "temperature": req.temperature,
    })

    add_message(req.session_id, "user", req.message)
    reply = run_agent(req.message, mem)
    add_message(req.session_id, "assistant", reply)

    add_log(req.session_id, {
        "ts": datetime.utcnow().isoformat(),
        "type": "response",
        "reply_preview": reply[:120],
    })

    return ChatResponse(reply=reply, memory=mem, logs=get_logs(req.session_id))

@app.post("/reset")
def reset(session_id: str):
    reset_session(session_id)
    return {"status": "reset", "session_id": session_id}

@app.get("/logs")
def logs(session_id: str):
    return {"session_id": session_id, "logs": get_logs(session_id)}
