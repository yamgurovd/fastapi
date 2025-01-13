from fastapi import FastAPI
import uvicorn

import sys
from pathlib import Path

# from src.database import *

sys.path.append(str(Path(__file__).parent.parent))
app = FastAPI()

from src.api.hotels import router as router_hotels
from src.api.auth import router as router_auth

app.include_router(router_auth)
app.include_router(router_hotels)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",  reload=True)
