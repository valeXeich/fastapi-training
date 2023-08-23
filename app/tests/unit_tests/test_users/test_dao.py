import pytest

from app.users.dao import UsersDAO


@pytest.mark.parametrize(
    "user_id,email,exists",
    [
        (1, "user1@example.com", True),
        (2, "user2@example.com", True),
        (5, "....", False),
    ],
)
async def test_find_user_by_id(user_id, email, exists):
    user = await UsersDAO.find_by_id(user_id)
    if exists:
        assert user
        assert user.id == user_id
        assert user.email == email
    else:
        assert not user
