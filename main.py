from fastapi import FastAPI, Request
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os

app = FastAPI()

# Load your key from env var set in Render
api_key = os.getenv("MISTRAL_API_KEY")
client = MistralClient(api_key=api_key, model="mistral-tiny")

@app.get("/")
def root():
    return {"message": "Server working 🔥"}

@app.post("/ocr")
async def ocr(request: Request):
    data = await request.json()
    prompt = data.get("text", "Hello from Mistral!")

    messages = [ChatMessage(role="user", content=prompt)]
    res = client.chat(messages=messages)

    return {"output": res.choices[0].message.content}
