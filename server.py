import asyncio
import json
from urllib import request
from fastapi import FastAPI
import uvicorn
from fastapi import Request
# from player_stats import Player_stats
import requests
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from backend import routes

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")
app.include_router(routes.router)


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8080, reload=True)
