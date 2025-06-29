from fastapi import FastAPI
from pydantic import BaseModel
from mistralai.async_client import AsyncMistralClient
from mistralai.models.chat_completion import ChatMessage
import os
import asyncio

app = FastAPI()

api_key = os.getenv("MISTRAL_API_KEY")
client = AsyncMistralClient(api_key=api_key)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat_with_mistral(req: PromptRequest):
    response = await client.chat(
        model="mistral-small-latest",
        messages=[ChatMessage(role="user", content=req.prompt)]
    )
    return {"response": response.choices[0].message.content}
