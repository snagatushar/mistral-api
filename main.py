from fastapi import FastAPI, Request
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os

app = FastAPI()

# Use environment variable for safety
api_key = os.getenv("MISTRAL_API_KEY")

# Create client using updated SDK
client = MistralClient(api_key=api_key, model="mistral-tiny")

@app.get("/")
def root():
    return {"message": "Mistral API is live!"}

@app.post("/ocr")
async def ocr(request: Request):
    body = await request.json()
    text_input = body.get("text", "Extract data from this image")

    messages = [ChatMessage(role="user", content=text_input)]
    response = client.chat(messages=messages)

    return {"response": response.choices[0].message.content}
