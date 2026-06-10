from fastapi import FastAPI
from pydantic import BaseModel

from graph import graph

from langchain_core.messages import HumanMessage

app = FastAPI()
class ChatRequest(BaseModel):
    question: str
# api endpoint for chat
@app.post("/chat")
def chat(data: ChatRequest):

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content=data.question
                )
            ]
        },
            config={
        "configurable": {
            "thread_id": "user1"
        }
    }

    )

    return {
        "response":
        result["messages"][-1].content
    }