# XYExcel Demo

This project demonstrates a simple Excel analysis assistant with a Vue front end and a FastAPI back end.

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   uvicorn server:app --reload
   ```
3. Open `index.html` in a browser (or serve it with any static server).

## Usage

1. Upload an Excel file using the file input.
2. Enter commands in the chat box. Supported commands are:
   - `sum <column>` – calculate the sum of a column.
   - `plot <x_column> <y_column>` – plot two columns and return a chart image.
3. Results appear in the chat area. Images are displayed inline.

This is a very small demo for local use and does not provide authentication or protection for arbitrary code execution.
