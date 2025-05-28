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

# import asyncio
# from contextlib import asynccontextmanager
#
# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
#
# from fastapi_cache import FastAPICache
# from fastapi_cache.backends.redis import RedisBackend
#
# import sys
# from pathlib import Path
#
# from src.api.dependencies import get_db
# from src.init import redis_manager
#
# # Adjust the system path to include the parent directory
# sys.path.append(str(Path(__file__).parent))
#
#
# # Create FastAPI instance
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # При старте приложения
#     await redis_manager.connect()
#     FastAPICache.init(RedisBackend(redis_manager.redis), prefix="fastapi-cache")
#     yield
#     await redis_manager.close()
#     # При выключении/перезагрузке приложения
#
#
# # Include routers for different modules
# from src.init import redis_manager
# from api.auth import router as router_auth  # Adjusted import path
# from api.hotels import router as router_hotels  # Adjusted import path
# from src.api.rooms import router as router_rooms
# from src.api.bookings import router as router_bookings
# from src.api.facilities import router as router_facilities
# from src.api.images import router as router_images
#
#
# async def send_emails_bookings_today_checkin():
#     async for db in get_db():
#         bookings = await db.bookings.get_bookings_with_today_checkin()
#         print(f"{bookings=}")
#
#
# async def run_send_email_regularly():
#     while True:
#         await send_emails_bookings_today_checkin()
#         await asyncio.sleep(5)
#
#
# app = FastAPI(lifespan=lifespan)
#
#
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # При старте приложения
#     asyncio.create_task(run_send_email_regularly())
#     await redis_manager.connect()
#     FastAPICache.init(RedisBackend(redis_manager.redis), prefix="fastapi-cache")
#
#
# app.include_router(router_auth)
# app.include_router(router_hotels)
# app.include_router(router_rooms)
# app.include_router(router_facilities)
# app.include_router(router_bookings)
# app.include_router(router_images)
#
# # Configure CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# # Mount static files directory
# app.mount("/static", StaticFiles(directory="static"), name="static")
#
# # Run the application with Uvicorn if this script is executed directly
# if __name__ == "__main__":
#     uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)  # Adjusted for module path
#
# # Запуск
# # uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
# # http://localhost:8000/static/login/auth.html - страница логирования
#

import asyncio
import sys
from pathlib import Path
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from src.api.dependencies import get_db
from src.init import redis_manager

# Корректировка путей
sys.path.append(str(Path(__file__).parent.parent))


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Инициализация при старте
    await redis_manager.connect()
    FastAPICache.init(RedisBackend(redis_manager._redis), prefix="fastapi-cache")

    # Фоновая задача с обработкой отмены
    task = asyncio.create_task(run_send_email_regularly())

    try:
        yield
    finally:
        # Корректное завершение
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass
        await redis_manager.close()


# Импорт роутеров (исправлены пути)
from src.api.auth import router as router_auth
from src.api.hotels import router as router_hotels
from src.api.rooms import router as router_rooms
from src.api.bookings import router as router_bookings
from src.api.facilities import router as router_facilities
from src.api.images import router as router_images

app = FastAPI(lifespan=lifespan)

# Подключение CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(router_auth, prefix="/api")
app.include_router(router_hotels, prefix="/api")
app.include_router(router_rooms, prefix="/api")
app.include_router(router_bookings, prefix="/api")
app.include_router(router_facilities, prefix="/api")
app.include_router(router_images, prefix="/api")

# Статические файлы
app.mount("/static", StaticFiles(directory="src/static"), name="static")


async def send_emails_bookings_today_checkin():
    async for db in get_db():
        bookings = await db.bookings.get_bookings_with_today_checkin()
        print(f"{bookings=}")


async def run_send_email_regularly():
    try:
        while True:
            await send_emails_bookings_today_checkin()
            await asyncio.sleep(5)
    except asyncio.CancelledError:
        print("Фоновая задача остановлена")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
