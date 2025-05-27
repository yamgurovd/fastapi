# import pytest
#
# from src.config import settings
# from src.database import Base, engine_null_pool
# from src.main import app
# from src.models import *
# from httpx import AsyncClient
#
#
# @pytest.fixture(scope="session", autouse=True)
# def check_test_mode():
#     assert settings.MODE == "TEST"
#
#
# @pytest.fixture(scope="session", autouse=True)
# async def setup_database(check_test_mode):
#     async with engine_null_pool.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#
#
# @pytest.fixture(scope="session", autouse=True)
# async def register_user(setup_database):
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         await ac.post(
#             "api/auth/register",
#             json={
#                 "email": "kot@pes.com",
#                 "password": "1234"
#             }
#         )

import json
from unittest import mock

mock.patch("fastapi_cache.decorator.cache", lambda *args, **kwargs: lambda f: f).start()

import pytest
from httpx import AsyncClient, ASGITransport

from src.schemas.hotels import HotelAdd
from src.schemas.rooms import RoomAdd
from src.utils.db_manager import DBManager

from src.config import settings
from src.database import Base, engine_null_pool, async_session_maker_null_pool
from src.main import app
from src.models import *   # noqa: F402, 403


@pytest.fixture(scope="session", autouse=True)
def check_test_mode():
    assert settings.MODE == "TEST"


@pytest.fixture(scope="function")
async def db() -> DBManager:
    async with DBManager(session_factory=async_session_maker_null_pool) as db:
        yield db


@pytest.fixture(scope="session", autouse=True)
async def setup_database(check_test_mode):
    async with engine_null_pool.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    with open("tests/mock_hotels.json", encoding="utf-8") as file_hotels:
        hotels = json.load(file_hotels)
    with open("tests/mock_rooms.json", encoding="utf-8") as file_rooms:
        rooms = json.load(file_rooms)

    hotels = [HotelAdd.model_validate(hotel) for hotel in hotels]
    rooms = [RoomAdd.model_validate(room) for room in rooms]

    async with DBManager(session_factory=async_session_maker_null_pool) as db_:
        await db_.hotels.add_bulk(hotels)
        await db_.rooms.add_bulk(rooms)
        await db_.commit()


@pytest.fixture(scope="session")
async def ac() -> AsyncClient:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="session", autouse=True)
async def register_user(setup_database):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/api/auth/register",  # Обратите внимание на префикс /api
            json={
                "email": "kot@pes.com",
                "password": "1234"
            }
        )
        assert response.status_code == 200 or response.status_code == 201, f"Registration failed: {response.text}"


@pytest.fixture(scope="session")
async def authenticated_ac(register_user, ac):
    await ac.post(
        "/auth/login",
        json={
            "email": "kot@pes.com",
            "password": "1234"
        }
    )
    assert ac.cookies["access_token"]
    yield ac
