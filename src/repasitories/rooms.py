from datetime import date

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import selectinload

from src.exceptions import RoomNotFoundException
from src.database import Base
from sqlalchemy import select, func
from src.database import engine
from src.models.bookings import BookingsOrm

from src.repasitories.utils import rooms_ids_for_booking
from src.repasitories.base import BaseRepository
from src.models.rooms import RoomsOrm
from src.repasitories.mappers.mappers import RoomDataMapper, RoomDataWithRelsMapper


class RoomsRepository(BaseRepository):
    model: RoomsOrm = RoomsOrm
    mapper = RoomDataMapper

    async def get_filtered_by_time(
        self,
        hotel_id,
        date_from: date,
        date_to: date,
    ):
        rooms_ids_to_get = rooms_ids_for_booking(date_from, date_to, hotel_id)
        query = (
            select(self.model) # type: ignore
            .options(selectinload(self.model.facilities))
            .filter(RoomsOrm.id.in_(rooms_ids_to_get)) # type: ignore
        )
        result = await self.session.execute(query)
        return [
            RoomDataWithRelsMapper.map_to_domain_entity(model)
            for model in result.unique().scalars().all()
        ]

    async def get_one_with_rels(self, **filter_by):
        query = (
            select(self.model) # type: ignore
            .options(selectinload(self.model.facilities)) # type: ignore
            .filter_by(**filter_by) # type: ignore
        )
        result = await self.session.execute(query)
        try:
            model = result.scalar_one()
        except NoResultFound:
            raise RoomNotFoundException
        return RoomDataWithRelsMapper.map_to_domain_entity(model)
