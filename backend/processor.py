import base64
import io
from typing import Dict, Any

import pandas as pd
import matplotlib.pyplot as plt


def process_message(message: str, df: pd.DataFrame) -> Dict[str, Any]:
    """Process a text command and return a response dict."""
    cmd, *args = message.strip().lower().split()
    if df is None:
        return {"type": "text", "content": "No Excel file uploaded."}
    if cmd == "sum" and args:
        col = args[0]
        if col in df.columns:
            result = df[col].sum()
            return {"type": "text", "content": f"Sum of {col}: {result}"}
        return {"type": "text", "content": f"Column {col} not found"}
    if cmd == "average" and args:
        col = args[0]
        if col in df.columns:
            result = df[col].mean()
            return {"type": "text", "content": f"Average of {col}: {result}"}
        return {"type": "text", "content": f"Column {col} not found"}
    if cmd == "plot" and args:
        col = args[0]
        if col in df.columns:
            fig, ax = plt.subplots()
            df[col].plot(kind="line", ax=ax, title=f"Plot of {col}")
            buf = io.BytesIO()
            plt.savefig(buf, format="png")
            plt.close(fig)
            data = base64.b64encode(buf.getvalue()).decode("utf-8")
            return {"type": "image", "content": f"data:image/png;base64,{data}"}
        return {"type": "text", "content": f"Column {col} not found"}
    return {"type": "text", "content": "Unknown command"}
