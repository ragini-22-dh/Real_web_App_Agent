import streamlit as st
import requests
import uuid

API_BASE = st.secrets.get("API_BASE", "http://localhost:8000")

st.set_page_config(page_title="AI Agent Dashboard", layout="wide")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "memory" not in st.session_state:
    st.session_state.memory = []

if "logs" not in st.session_state:
    st.session_state.logs = []

st.title("🧠 AI Agent Dashboard")

# Sidebar controls
st.sidebar.header("Controls")
model = st.sidebar.text_input("Model", value="gpt-4o-mini")
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.2, 0.1)

colA, colB = st.sidebar.columns(2)
if colA.button("Reset Memory"):
    requests.post(f"{API_BASE}/reset", params={"session_id": st.session_state.session_id})
    st.session_state.memory = []
    st.session_state.logs = []
    st.sidebar.success("Reset done ✅")

if colB.button("Health"):
    r = requests.get(f"{API_BASE}/health").json()
    st.sidebar.info(r.get("status", "unknown"))

tab_chat, tab_memory, tab_logs = st.tabs(["💬 Chat", "🧾 Memory", "📜 Logs"])

with tab_chat:
    st.subheader("Chat")
    for m in st.session_state.memory:
        with st.chat_message(m["role"]):
            st.write(m["content"])

    user_msg = st.chat_input("Type your message...")
    if user_msg:
        payload = {
            "session_id": st.session_state.session_id,
            "message": user_msg,
            "temperature": temperature,
            "model": model,
        }
        res = requests.post(f"{API_BASE}/chat", json=payload).json()
        st.session_state.memory = res.get("memory", [])
        st.session_state.logs = res.get("logs", [])
        st.rerun()

with tab_memory:
    st.subheader("Current Memory")
    st.json(st.session_state.memory)

with tab_logs:
    st.subheader("Run Logs")
    st.json(st.session_state.logs)
