import base64
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt

class ExcelProcessor:
    def __init__(self):
        self.df = None

    def set_dataframe(self, df: pd.DataFrame):
        self.df = df

    def process(self, command: str):
        if self.df is None:
            return {"type": "text", "content": "No Excel file uploaded."}
        if not command:
            return {"type": "text", "content": "Empty command."}
        parts = command.strip().split()
        if not parts:
            return {"type": "text", "content": "Empty command."}
        action = parts[0].lower()
        if len(parts) < 2:
            return {"type": "text", "content": "Please specify a column."}
        column = parts[1]
        if column not in self.df.columns:
            return {"type": "text", "content": f'Column "{column}" not found.'}
        if action == 'sum':
            result = self.df[column].sum()
            return {"type": "text", "content": f'Sum of {column}: {result}'}
        if action == 'average':
            result = self.df[column].mean()
            return {"type": "text", "content": f'Average of {column}: {result}'}
        if action == 'plot':
            fig, ax = plt.subplots()
            self.df[column].plot(ax=ax)
            ax.set_title(column)
            buf = BytesIO()
            fig.savefig(buf, format='png')
            plt.close(fig)
            data = base64.b64encode(buf.getvalue()).decode('utf-8')
            return {"type": "image", "content": data}
        return {"type": "text", "content": 'Unknown command.'}
