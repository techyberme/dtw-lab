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
# In iti al ize FastAPI a p p l i c a t i o n instance
# This creates our main a p p l i c a t i o n object that will handle
#all routing and middleware
app = FastAPI()
# Server d ep loy me nt c o n f i g u r a t i o n function . We specify on
#what port we serve , and what IPs we listen to .
def run_server(port:int=80 , reload : bool = False , host :
    str = "127.0.0.1" ) :
    uvicorn.run ("dtw_lab.lab2:app" , port = port , reload = reload ,
    host = host )
# Define an entry point to our a p p l i c a t i o n .
@app.get("/" )
def main_route():
    return {"message":"Hello world"}
@app.get("/statistic/{measure}/{column}")
def get_statistic( measure : str , column : str ) :
    df = read_csv_from_google_drive('1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo')
    df = clean_data(df)
    return calculate_statistic(measure,df[column])
@app.get("/visualize/{graph_type}")
def get_visualization(graph_type: str):
    df = read_csv_from_google_drive('1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo')
    df = clean_data(df)
    visualize_data(df)
    return FileResponse(f"graphs/{graph_type}.png")
@app.get("/version")
def get_visualization_version():
    """Extracts the version from pyproject.toml using toml library."""
    pyproject = toml.load("pyproject.toml")
    version = pyproject.get("tool", {}).get("poetry", {}).get("version", "Version not found")
    return {"version": version}