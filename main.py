from fastapi import FastAPI
from pydantic import BaseModel
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os

app = FastAPI()

# Load API key from environment
api_key = os.getenv("MISTRAL_API_KEY")
client = MistralClient(api_key=api_key, model="mistral-small-latest")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat_with_mistral(req: PromptRequest):
    response = client.chat(
        messages=[ChatMessage(role="user", content=req.prompt)]
    )
    return {"response": response.choices[0].message.content}
