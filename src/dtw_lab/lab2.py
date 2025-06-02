import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
import toml
from fastapi.responses import JSONResponse
from dtw_lab.lab1 import (
    read_csv_from_google_drive,
    visualize_data,
    calculate_statistic,
    clean_data,
)

app = FastAPI()


def run_server(port: int = 80, reload: bool = False, host: str = "127.0.0.1"):
    uvicorn.run("dtw_lab.lab2:app", port=port, reload=reload, host=host)


@app.get("/")
def main_route():
    return {"message": "Hello world"}
@app.get("/statistic/{measure}/{column}")
def get_statistic(measure: str, column: str):
    df = read_csv_from_google_drive('1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo')
    df = clean_data(df)
    calculate_statistic('measure',df[column])
@app.get("/visualize/{graph_type}")
def get_visualization(graph_type: str):
    df = read_csv_from_google_drive('1eKiAZKbWTnrcGs3bqdhINo1E4rBBpglo')
    df = clean_data(df)
    visualize_data(df)
    return FileResponse("graphs/{graph_type}.png", filename="{graph_type}.png")
@app.get("/version")
def get_visualization_version():
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    if not pyproject_path.exists():
        return JSONResponse(status_code=404, content={"error": "pyproject.toml not found"})

    pyproject_data = toml.load(pyproject_path)
    version = pyproject_data.get("tool", {}).get("poetry", {}).get("version")

    if version is None:
        return JSONResponse(status_code=500, content={"error": "Version not found in pyproject.toml"})

    return {"version": version}