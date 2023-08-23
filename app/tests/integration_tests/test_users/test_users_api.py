import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("kot@pes.com", "kotopes", 200),
        ("kot@pes.com", "kot0pes", 409),
        ("abcde", "pesoket", 422),
    ],
)
async def test_register_user(email, password, status_code, async_client: AsyncClient):
    response = await async_client.post(
        "/auth/register",
        json={
            "email": email,
            "password": password,
        },
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("user1@example.com", "user1", 200),
        ("user2@example.com", "user2", 200),
        ("wrong@person.com", "wrong", 401),
    ],
)
async def test_login_user(email, password, status_code, async_client: AsyncClient):
    response = await async_client.post(
        "/auth/login",
        json={
            "email": email,
            "password": password,
        },
    )
    assert response.status_code == status_code
