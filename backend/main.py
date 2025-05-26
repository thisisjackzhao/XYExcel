from fastapi import FastAPI, UploadFile, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from processor import ExcelProcessor
from fastapi import FastAPI, UploadFile, File, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

from .processor import process_message

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

processor = ExcelProcessor()

@app.post('/upload')
async def upload(file: UploadFile):
    data = await file.read()
    processor.load(data)
    return {'status': 'ok'}

@app.websocket('/ws')
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        text = await ws.receive_text()
        result = processor.execute(text)
        await ws.send_json(result)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage of the uploaded Excel data
DATA = {
    "df": None
}

@app.post("/upload")
async def upload_excel(file: UploadFile = File(...)):
    content = await file.read()
    DATA["df"] = pd.read_excel(content)
    return {"status": "uploaded", "columns": list(DATA["df"].columns)}

@app.get("/")
async def root():
    return HTMLResponse("<h1>XYExcel Backend</h1>")

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            data = await ws.receive_text()
            response = process_message(data, DATA["df"])
            await ws.send_json(response)
    except WebSocketDisconnect:
        pass
