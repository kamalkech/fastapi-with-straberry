"""..."""

from typing import List
from fastapi import HTTPException

from app.user.model import UserType
from app.user.dto import UserCreateInput

users: List[UserType] = [
    UserType(
        name="John",
        email="a@a.com",
        password="1234"
    ),
    UserType(
        name="Jane",
        email="b@b.com",
        password="1234"
    )
]


class UserService:
    """..."""

    @staticmethod
    def get_users() -> List[UserType]:
        """..."""
        return users

    @staticmethod
    def get_user_by_email(email: str) -> UserType:
        """..."""

        user_exist = None
        for user in users:
            if user.email == email:
                user_exist = user

        print("Result", user_exist)
        if user_exist is None:
            raise HTTPException(status_code=404, detail="Item not found")

        return user_exist

    @staticmethod
    def create_user(user_input: UserCreateInput) -> UserType:
        """...."""
        new_user = UserType(
            name=user_input.name,
            email=user_input.email,
            password=user_input.password
        )
        users.append(new_user)

        return new_user
