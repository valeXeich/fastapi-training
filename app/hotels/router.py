from datetime import date

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.hotels.dao import HotelDAO
from app.hotels.rooms.dao import RoomDAO
from app.hotels.rooms.schemas import SRoomInfo
from app.hotels.schemas import SHotel

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/{location}")
@cache(expire=60 * 60)
async def get_hotels(location: str, date_from: date, date_to: date) -> list[SHotel]:
    hotels = await HotelDAO.find_all(location, date_from, date_to)
    return hotels


@router.get("/{hotel_id}/rooms")
@cache(expire=60 * 60)
async def get_rooms_by_time(
    hotel_id: int,
    date_from: date,
    date_to: date,
) -> list[SRoomInfo]:
    rooms = await RoomDAO.find_all(hotel_id, date_from, date_to)
    return rooms
