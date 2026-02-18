from fastapi import FastAPI, Request
from ai_pipeline import process_text

app = FastAPI()

@app.post("/process")
async def process(request: Request):
    text = await request.body()
    text = text.decode("utf-8")
    result = process_text(text)
    return {"result": result}
