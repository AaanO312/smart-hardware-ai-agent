"""FastAPI 接口：将 Agent 包装为 REST API"""
import json
import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from agent.react_agent import ReactAgent

app = FastAPI(title="智扫通 AI Agent API")

agent = ReactAgent()


class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
async def chat(req: ChatRequest):
    """对话接口：真正的 SSE 流式返回"""

    async def event_generator():
        # execute_stream 是同步生成器，用 to_thread 避免阻塞事件循环
        sync_gen = agent.execute_stream(req.question)

        while True:
            try:
                chunk = await asyncio.to_thread(next, sync_gen)
                yield f"data: {json.dumps({'content': chunk}, ensure_ascii=False)}\n\n"
            except StopIteration:
                break

    return StreamingResponse(event_generator(), media_type="text/event-stream")


@app.get("/health")
def health():
    return {"status": "ok"}
