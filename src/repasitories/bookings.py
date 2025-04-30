from src.models.bookings import BookingsOrm
from src.repasitories.base import BaseRepository
from src.repasitories.mappers.mappers import BookingDataMapper
from src.schemas.bookings import Booking


class BookingsRepository(BaseRepository):
    model = BookingsOrm
    mapper = BookingDataMapper