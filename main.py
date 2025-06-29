import os
from fastapi import FastAPI
from pydantic import BaseModel
from mistralai.client import MistralClient
from mistralai.models.ocr import OcrDocument

app = FastAPI()

# Use environment variable for security
client = MistralClient(api_key=os.getenv("MISTRAL_API_KEY"))

class OCRInput(BaseModel):
    file_base64: str

@app.post("/ocr")
def extract_text(data: OCRInput):
    # Remove prefix from base64 string
    base64_data = data.file_base64.split(",")[1]
    document = OcrDocument(document_base64=base64_data)
    result = client.ocr.process(document=document)
    return {"text": result.markdown}
