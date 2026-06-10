"""FastAPI 接口：将 Agent 包装为 REST API"""
from fastapi import FastAPI
from pydantic import BaseModel
from agent.react_agent import ReactAgent

app = FastAPI(title="智扫通 AI Agent API")

agent = ReactAgent()


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    """对话接口：输入问题，返回 Agent 回答"""
    result = []
    for chunk in agent.execute_stream(req.question):
        result.append(chunk)
    return ChatResponse(answer="".join(result))


@app.get("/health")
def health():
    return {"status": "ok"}
