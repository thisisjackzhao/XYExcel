from fastapi import FastAPI, File, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = None

@app.post('/upload')
async def upload(file: UploadFile = File(...)):
    global df
    content = await file.read()
    df = pd.read_excel(io.BytesIO(content))
    return {"status": "uploaded", "columns": list(df.columns)}

@app.websocket('/ws')
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            data = await ws.receive_text()
            result = process_message(data)
            await ws.send_json(result)
    except WebSocketDisconnect:
        pass

def process_message(message: str):
    global df
    if df is None:
        return {"type": "text", "data": "Please upload an Excel file first."}
    message = message.strip().lower()
    if message.startswith('sum '):
        col = message[4:].strip()
        if col in df.columns:
            s = df[col].sum()
            return {"type": "text", "data": f"Sum of {col}: {s}"}
        else:
            return {"type": "text", "data": f"Column {col} not found."}
    if message.startswith('plot '):
        parts = message.split()
        if len(parts) >= 3:
            x, y = parts[1], parts[2]
            if x in df.columns and y in df.columns:
                plt.figure()
                df.plot(x=x, y=y)
                plt.tight_layout()
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                plt.close()
                encoded = base64.b64encode(buf.getvalue()).decode('utf-8')
                return {"type": "image", "data": encoded}
            else:
                return {"type": "text", "data": "Columns not found."}
        return {"type": "text", "data": "Usage: plot <x> <y>"}
    return {"type": "text", "data": "Unknown command."}
