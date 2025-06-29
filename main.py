from fastapi import FastAPI, Request
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os

app = FastAPI()

# Initialize Mistral client with your API key from env variable
client = MistralClient(
    api_key=os.getenv("MISTRAL_API_KEY"),
    model="mistral-tiny"  # or mistral-small / mistral-medium
)

@app.get("/")
def home():
    return {"message": "Mistral API is running!"}

@app.post("/ocr")
async def ocr(request: Request):
    data = await request.json()
    user_input = data.get("text", "Hello from Render!")

    response = client.chat(
        messages=[
            ChatMessage(role="user", content=user_input)
        ]
    )

    return {"response": response.choices[0].message.content}
