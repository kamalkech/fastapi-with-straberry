"""..."""
from typing import List
from fastapi import HTTPException

from app.user.type import UserType, UserCreateInput

users: List[UserType] = [
    UserType(
        id=1,
        name="John",
        email="a@a.com"
    ),
    UserType(
        id=2,
        name="Jane",
        email="b@b.com"
    )
]


def get_users() -> List[UserType]:
    """..."""
    return users


def get_user_by_id(user_id: int) -> UserType:
    """..."""
    user_exist = None
    for user in users:
        print("PRINT:", user.id, user_id)
        if user.id == user_id:
            user_exist = user

    print("Result", user_exist)
    if user_exist is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return user_exist


def create_user(user_input: UserCreateInput) -> UserType:
    """..."""
    new_user = UserType(
        id=len(users) + 1,
        name=user_input.name,
        email=user_input.email
    )
    users.append(new_user)

    return new_user
