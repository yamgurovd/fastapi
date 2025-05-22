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


import pytest
from httpx import AsyncClient, ASGITransport

from src.config import settings
from src.database import Base, engine_null_pool
from src.main import app
from src.models import *


@pytest.fixture(scope="session", autouse=True)
def check_test_mode():
    assert settings.MODE == "TEST"


@pytest.fixture(scope="session", autouse=True)
async def setup_database(check_test_mode):
    async with engine_null_pool.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


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
