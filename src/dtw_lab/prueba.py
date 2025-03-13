import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
import toml
from dtw_lab.lab1 import (
    read_csv_from_google_drive,
    visualize_data ,
    calculate_statistic,
    clean_data ,
)
df = read_csv_from_google_drive('1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo')
df = clean_data(df)
df