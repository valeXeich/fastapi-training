import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "room_id, date_from, date_to, booked_rooms, status_code",
    *[
        [(4, "2030-12-01", "2030-12-30", i, 200) for i in range(3, 11)]
        + [(4, "2030-12-01", "2030-12-30", 10, 409)] * 2
    ],
)
async def test_add_and_get_booking(
    room_id,
    date_from,
    date_to,
    booked_rooms,
    status_code,
    authenticated_async_client: AsyncClient,
):
    response = await authenticated_async_client.post(
        "/bookings",
        params={
            "room_id": room_id,
            "date_from": date_from,
            "date_to": date_to,
        },
    )

    assert response.status_code == status_code

    response = await authenticated_async_client.get("/bookings")

    assert len(response.json()) == booked_rooms


async def test_get_and_delete_user_bookings(authenticated_async_client: AsyncClient):
    user_bookings = await authenticated_async_client.get("/bookings")

    for booking in user_bookings.json():
        await authenticated_async_client.delete(f'bookings/{booking["id"]}')

    user_bookings = await authenticated_async_client.get("/bookings")

    assert user_bookings.status_code == 200
    assert user_bookings.json() == []
