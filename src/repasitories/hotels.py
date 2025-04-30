from datetime import date

from sqlalchemy import select, func

from src.models.rooms import RoomsOrm
from src.repasitories.base import BaseRepository
from src.models.hotels import HotelsOrm
from src.repasitories.mappers.mappers import HotelDataMapper
from src.repasitories.utils import rooms_ids_for_booking
from src.schemas.hotels import Hotel


class HotelsRepository(BaseRepository):
    model = HotelsOrm
    mapper = HotelDataMapper

    async def get_filtered_by_time(
            self,
            date_from: date,
            date_to: date,
            location,
            title,
            limit,
            offset,
    ) -> list[Hotel]:
        rooms_ids_to_get = rooms_ids_for_booking(date_from=date_from, date_to=date_to)
        hotels_ids_to_get = (
            select(RoomsOrm.hotel_id)
            .select_from(RoomsOrm)
            .filter(RoomsOrm.id.in_(rooms_ids_to_get))
        )
        query = select(HotelsOrm).filter(HotelsOrm.id.in_(hotels_ids_to_get))
        if location:
            query = query.filter(func.lower(HotelsOrm.location).contains(location.strip().lower()))
        if title:
            query = query.filter(func.lower(HotelsOrm.title).contains(title.strip().lower()))
            query = (
                query
                .limit(limit)
                .offset(offset)
            )
            print(query.compile(compile_kwargs={"literal_binds": True}))
            result = await self.session.execute(query)
            return [self.mapper.map_to_domain_entity(hotel) for hotel in result.scalars().all()]
