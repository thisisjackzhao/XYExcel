from fastapi import FastAPI, WebSocket, WebSocketDisconnect, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

from .processor import ExcelProcessor

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

processor = ExcelProcessor()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    data = await file.read()
    df = pd.read_excel(data)
    processor.set_dataframe(df)
    return {"status": "uploaded"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            msg = await ws.receive_text()
            result = processor.process(msg)
            await ws.send_json(result)
    except WebSocketDisconnect:
        pass
