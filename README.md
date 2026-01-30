# AI Agent Dashboard — Full Stack Web App

A production-style AI agent web application built with Streamlit and FastAPI, powered by the OpenAI API and deployed in the cloud.

This project demonstrates how to design, deploy, and operate an LLM-powered agent system with a real backend, UI, session memory, structured logs, and secure secret management.

---

## Live Demo

Frontend: https://realwebappagent-hvn6uwtzksznev6fmdmshh.streamlit.app 


Backend API: https://real-web-app-agent.onrender.com

---

## Features

- Chat-based AI agent interface  
- Server-side session memory  
- Execution logs and observability  
- Model and temperature controls  
- Reset session functionality  
- Cloud deployment (Render for backend, Streamlit Cloud for frontend)  
- Secure API key handling via environment variables  

---

## Architecture

Streamlit UI  
→ FastAPI backend  
→ OpenAI API  

The frontend communicates only with the FastAPI backend. All OpenAI calls and secrets remain server-side.

---

## Technology Stack

- Python  
- Streamlit  
- FastAPI  
- OpenAI API  
- Render (backend hosting)  
- Streamlit Community Cloud (frontend)  
- python-dotenv  
- REST APIs  

---

## Repository Structure

week10-agent-dashboard/
├── backend/  
│   ├── main.py  
│   ├── agent.py  
│   ├── memory.py  
│   ├── models.py  
│   └── requirements.txt  
├── frontend/  
│   ├── app.py  
│   └── requirements.txt  
├── .gitignore  
└── README.md  

---

## Running Locally

### Backend

cd backend  
python -m venv .venv  
source .venv/bin/activate  
pip install -r requirements.txt  
uvicorn main:app --reload --port 8000  

Create backend/.env:

OPENAI_API_KEY=your_key_here  
OPENAI_MODEL=gpt-4.1-mini  

---

### Frontend

cd frontend  
python -m venv .venv  
source .venv/bin/activate  
pip install -r requirements.txt  
streamlit run app.py  

Create frontend/.streamlit/secrets.toml:

API_BASE = "http://localhost:8000"

---

## Deployment

### Backend on Render

Root directory: backend  
Build command: pip install -r requirements.txt  
Start command: uvicorn main:app --host 0.0.0.0 --port $PORT  

Environment variables:

OPENAI_API_KEY  
OPENAI_MODEL  

---

### Frontend on Streamlit Cloud

Add Streamlit secrets:

API_BASE = https://real-web-app-agent.onrender.com

---

## Demo Video

https://youtu.be/2niAkoyoYNE

---

## What This Project Demonstrates

- Full-stack AI engineering  
- API-based LLM orchestration  
- Stateful agents  
- Logging and monitoring  
- Cloud deployment  
- Secure configuration  
- UI-driven ML systems  

