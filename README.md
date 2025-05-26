# XYExcel

XYExcel is a small demo project for analyzing Excel files through a chat interface.
The backend is built with **FastAPI** and the frontend uses **Vue 3** with plain
HTML. Communication happens over WebSockets and the backend supports simple
commands like `sum`, `average` and `plot` on uploaded Excel columns.

## Structure

```
backend/   Python FastAPI application
frontend/  Static Vue app
```

## Setup

1. Install Python dependencies (FastAPI, pandas, matplotlib, uvicorn):
   ```bash
   pip install fastapi pandas matplotlib uvicorn
   ```
2. Run the backend:
   ```bash
   uvicorn backend.main:app --reload
   ```
3. Open `frontend/index.html` in a browser. Use the file input to upload an
   Excel file and send commands in the chat box (e.g. `sum Amount`).

The server responds with text or plots which are displayed in the chat.
