from sqlalchemy import select
from pydantic import EmailStr
from src.repasitories.base import BaseRepository
from src.models.users import UsersOrm
from src.schemas.users import User, UserWithHashedPassword


class UsersRepository(BaseRepository):
    model = UsersOrm
    schema = User

    # async def get_user_with_hashed_password(self, email: EmailStr):
    #     query = select(self.model).filter_by(email=email)
    #     result = await self.session.execute(query)
    #     model = result.scalars().one()
    #     return UserWithHashedPassword.model_validate(model)

    async def get_user_with_hashed_password(self, email: EmailStr):
        query = select(self.model).filter_by(email=email)
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()  # Change here
        if model is None:
            return None  # Handle case where user is not found
        return UserWithHashedPassword.model_validate(model)
