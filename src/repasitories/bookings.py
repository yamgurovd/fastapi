from datetime import date

from sqlalchemy import select

from src.models.bookings import BookingsOrm
from src.repasitories.base import BaseRepository
from src.repasitories.mappers.mappers import BookingDataMapper
from src.schemas.bookings import Booking


class BookingsRepository(BaseRepository):
    model = BookingsOrm
    mapper = BookingDataMapper

    async def get_bookings_with_today_checkin(self):
        query = (
            select(BookingsOrm)
            .filter(BookingsOrm.date_from == date.today())
        )
        res = await self.session.execute(query)
        return [self.mapper.map_to_domain_entity(booking) for booking in res.scalars().all()]
