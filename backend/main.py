from fastapi import FastAPI, UploadFile, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from processor import ExcelProcessor

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
