from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from sqlalchemy import create_engine, Column, Integer, Text, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# 1. Database Connection String pointing to your Docker Container
# Ensure your password and db name perfectly match what is inside your docker-compose.yml
DATABASE_URL = "postgresql+psycopg2://postgres:yoursecurepassword@localhost:5432/ollama_db"



engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define a table structure to log AI chat interactions
class ChatHistory(Base):
    __tablename__ = "chat_history"
    id = Column(Integer, primary_key=True, index=True)
    user_prompt = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)

# Automatically create the table inside the running Docker container on launch
Base.metadata.create_all(bind=engine)

# 2. FastAPI Application Setup
app = FastAPI(title="FastAPI + PostgreSQL Docker")

# Allows your React Vite frontend to talk directly to your endpoints
app.add_middleware (
    CORSMiddleware,
    allow_origins=[
        "http://localhost:58612",  # Your actual React application port
        "http://127.0.0.1:58612"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryPayload(BaseModel):
    prompt: str

# Dependency hook to yield clean database sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 3. API Route testing Database Integration + Ollama Communication
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "FastAPI AI full-stack backend is running perfectly!"
    }

@app.post("/api/generate")
async def chat_with_ai(payload: QueryPayload, db: Session = Depends(get_db)):
    # Constructing payloads targeting local Ollama client engine
    ollama_payload = {
        "model": "llama3", 
        "prompt": payload.prompt,
        "stream": False
    }    
    try:
        # 1. Request processing through Ollama
        response = requests.post(OLLAMA_ENDPOINT, json=ollama_payload, timeout=None)
        response.raise_for_status()
        ai_reply = response.json().get("response", "")
        
        # 2. Persisting transaction records straight to PostgreSQL container
        db_record = ChatHistory(user_prompt=payload.prompt, ai_response=ai_reply)
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        
        return {
            "status": "success",
            "log_id": db_record.id,
            "result": ai_reply
        }
        
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=503, detail="Ollama application daemon is not running.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
