from fastapi import FastAPI
import uvicorn

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
app = FastAPI()

from src.api.hotels import router as router_hotels

app.include_router(router_hotels)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
