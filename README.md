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


## Usage

1. Upload an Excel file using the file input.
2. Enter commands in the chat box. Supported commands are:
   - `sum <column>` – calculate the sum of a column.
   - `plot <x_column> <y_column>` – plot two columns and return a chart image.
3. Results appear in the chat area. Images are displayed inline.

This is a very small demo for local use and does not provide authentication or protection for arbitrary code execution.
