from fastapi import FastAPI
from pydantic import BaseModel
from mistralai.client import MistralClient

app = FastAPI()
client = MistralClient(api_key="your_mistral_api_key")

class OCRInput(BaseModel):
    file_base64: str

@app.post("/ocr")
def process_ocr(data: OCRInput):
    base64_data = data.file_base64.split(",")[1]  # Remove data: prefix
    result = client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type": "document_base64",
            "document_base64": base64_data
        }
    )
    return {"text": result.markdown}
