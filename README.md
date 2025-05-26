# XYExcel

This project demonstrates a simple AI assistant that performs basic analysis on an uploaded Excel file. A Python FastAPI backend accepts the Excel file and processes user commands over WebSockets. The Vue frontend allows uploading the file and interacting with the backend in real time.

## Backend

Install dependencies and start the server:

```bash
pip install fastapi uvicorn pandas matplotlib openpyxl
uvicorn backend.main:app --reload
```

The backend exposes:

- `POST /upload` &ndash; upload an Excel file.
- `WS /ws` &ndash; send commands such as `sum <column>`, `average <column>` or `plot <column>`.

## Frontend

Serve the contents of the `frontend` folder or simply open `frontend/index.html` in a browser. You can use a simple HTTP server:

```bash
python3 -m http.server --directory frontend 8000
```

Open the page at `http://localhost:8000` and start chatting. Uploaded files are processed by the backend and textual or image results are displayed in the chat area.
