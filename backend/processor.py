import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

class ExcelProcessor:
    def __init__(self):
        self.df = None

    def load(self, file_bytes: bytes):
        self.df = pd.read_excel(BytesIO(file_bytes))

    def execute(self, command: str):
        if self.df is None:
            return {"type": "text", "data": "No file uploaded."}
        parts = command.strip().split()
        if not parts:
            return {"type": "text", "data": "Empty command."}
        action = parts[0].lower()
        if action == 'sum' and len(parts) > 1:
            col = parts[1]
            if col in self.df.columns:
                result = self.df[col].sum()
                return {"type": "text", "data": f"Sum of {col}: {result}"}
        if action == 'average' and len(parts) > 1:
            col = parts[1]
            if col in self.df.columns:
                result = self.df[col].mean()
                return {"type": "text", "data": f"Average of {col}: {result}"}
        if action == 'plot' and len(parts) > 1:
            col = parts[1]
            if col in self.df.columns:
                fig, ax = plt.subplots()
                self.df[col].plot(kind='line', ax=ax)
                buf = BytesIO()
                plt.savefig(buf, format='png')
                plt.close(fig)
                data = base64.b64encode(buf.getvalue()).decode('utf-8')
                return {"type": "image", "data": f"data:image/png;base64,{data}"}
        return {"type": "text", "data": "Unsupported command."}

