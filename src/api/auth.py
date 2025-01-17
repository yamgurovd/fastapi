from datetime import datetime, timezone, timedelta

from fastapi import APIRouter, HTTPException, Response, Request
from passlib.context import CryptContext
import jwt

from src.repasitories.users import UsersRepository
from src.database import async_session_maker
from src.schemas.users import UserRequestAdd, UserAdd
from src.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Авторизация и аутентификация"])


@router.post("/register")
async def register_user(data: UserRequestAdd):
    hashed_password = hashed_password = AuthService().hash_password(data.password)
    new_user_data = UserAdd(email=data.email, hashed_password=hashed_password)
    async with async_session_maker() as session:
        await UsersRepository(session).add(new_user_data)
        await session.commit()  # Ensure changes are committed
    return {"status": "OK"}


@router.post("/login")
async def login_user(data: UserRequestAdd, response: Response):
    print(f"Attempting login for email: {data.email}")
    async with async_session_maker() as session:
        user = await UsersRepository(session).get_user_with_hashed_password(email=data.email)

        if user is None:
            print("User not found.")
            raise HTTPException(status_code=401, detail="Пользователь с таким email не зарегистрирован")

        if not AuthService().verify_password(data.password, user.hashed_password):
            print("Password verification failed.")
            raise HTTPException(status_code=401, detail="Пароль неверный")

        access_token = AuthService().create_access_token({"user_id": user.id})
        response.set_cookie("access_token", access_token)
        return {"access_token": access_token}


@router.get("/only_auth")
async def login_user(
        request: Request,
):
    access_token = request.cookies.get("access_token", None)
    data = AuthService().encode_token(access_token)
    user_id = data["user_id"]
    async with async_session_maker() as session:
        user = await UsersRepository(session).get_one_or_none(id=user_id)
        return user
