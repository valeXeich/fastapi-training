from datetime import date

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.exceptions import RoomCannotBeBookedException
from app.tasks.tasks import send_booking_confiramtion_email
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.get("")
@cache(expire=60 * 60)
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    bookings = await BookingDAO.find_all(user_id=user.id)
    return bookings


@router.post("")
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBookedException
    send_booking_confiramtion_email.delay(booking, user.email)


@router.delete("/{booking_id}", status_code=204)
async def remove_booking(
    booking_id: int,
    user: Users = Depends(get_current_user),
):
    await BookingDAO.delete(id=booking_id, user_id=user.id)
