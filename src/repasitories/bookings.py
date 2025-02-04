from src.models.bookings import BookingsOrm
from src.repasitories.base import BaseRepository
from src.schemas.bookings import Booking


class BookingsRepository(BaseRepository):
    model = BookingsOrm
    schema = Booking
