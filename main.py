import os
from fastapi import FastAPI
from pydantic import BaseModel
from mistralai import MistralClient
from mistralai.models.ocr import OcrDocument

app = FastAPI()

client = MistralClient(api_key=os.getenv("7jjAfAK1zm9fodF0U9zREn5MqT7KIInX"))

class OCRInput(BaseModel):
    file_base64: str

@app.post("/ocr")
def process_ocr(data: OCRInput):
    base64_data = data.file_base64.split(",")[1]
    document = OcrDocument(document_base64=base64_data)
    result = client.ocr.process(document=document)
    return {"text": result.markdown}
