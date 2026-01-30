from typing import Dict, List

# For demo: in-memory store. For production: Redis/DB.
_SESSIONS: Dict[str, List[dict]] = {}
_LOGS: Dict[str, List[dict]] = {}

def get_memory(session_id: str) -> List[dict]:
    return _SESSIONS.setdefault(session_id, [])

def add_message(session_id: str, role: str, content: str) -> None:
    mem = _SESSIONS.setdefault(session_id, [])
    mem.append({"role": role, "content": content})

def get_logs(session_id: str) -> List[dict]:
    return _LOGS.setdefault(session_id, [])

def add_log(session_id: str, event: dict) -> None:
    logs = _LOGS.setdefault(session_id, [])
    logs.append(event)

def reset_session(session_id: str) -> None:
    _SESSIONS[session_id] = []
    _LOGS[session_id] = []
