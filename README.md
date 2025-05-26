# XYExcel

This project demonstrates a small Excel analysis tool with a Python FastAPI backend and a Vue 3 frontend.

## Backend

The backend exposes an upload route and a WebSocket for commands.

```bash
pip install fastapi uvicorn pandas matplotlib openpyxl
python backend/main.py
```

Commands supported over the WebSocket:
- `sum <column>` – calculate column sum
- `average <column>` – calculate column average
- `plot <column>` – return a line plot as an image

## Frontend

Open `frontend/index.html` in a browser after starting the backend. The frontend is structured using Vue components loaded as ES modules.

1. Upload an Excel file.
2. Enter commands in the chat box.
3. Text or image results are displayed in real time.
