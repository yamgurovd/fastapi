# from fastapi import FastAPI
# import uvicorn
#
# import sys
# from pathlib import Path
#
# # from src.database import *
#
# sys.path.append(str(Path(__file__).parent.parent))
# app = FastAPI()
#
# from src.api.hotels import router as router_hotels
# from src.api.auth import router as router_auth
#
# app.include_router(router_auth)
# app.include_router(router_hotels)
#
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0",  reload=True)

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

import sys
from pathlib import Path

from src.init import redis_manager

# Adjust the system path to include the parent directory
sys.path.append(str(Path(__file__).parent))


# Create FastAPI instance
@asynccontextmanager
async def lifespan(app: FastAPI):
    # При старте приложения
    await redis_manager.connect()
    FastAPICache.init(RedisBackend(redis_manager.redis), prefix="fastapi-cache")
    yield
    await redis_manager.close()
    # При выключении/перезагрузке приложения


# Include routers for different modules
from api.auth import router as router_auth  # Adjusted import path
from api.hotels import router as router_hotels  # Adjusted import path
from src.api.rooms import router as router_rooms
from src.api.bookings import router as router_bookings
from src.api.facilities import router as router_facilities

app = FastAPI(lifespan=lifespan)
app.include_router(router_auth)
app.include_router(router_hotels)
app.include_router(router_rooms)
app.include_router(router_facilities)
app.include_router(router_bookings)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Run the application with Uvicorn if this script is executed directly
if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)  # Adjusted for module path

# Запуск
# uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
# http://localhost:8000/static/login/auth.html - страница логирования
#
