"""..."""

import strawberry
from passlib.context import CryptContext

from app.middleware.jwt_manager import JWTManager


hash_pass = CryptContext(schemes=["bcrypt"], deprecated="auto")
list_users = [
    {
        "name": "root",
        "email": "root@email.com",
        "password": hash_pass.hash("root")
    },
    {
        "name": "admin",
        "email": "admin@email.com",
        "password": hash_pass.hash("admin")
    }
]


@strawberry.type
class UserType:
    """..."""
    name: str
    email: str
    password: str


@strawberry.input
class RegisterInput:
    """..."""

    name: str
    email: str
    password: str


@strawberry.input
class LoginInput:
    """..."""

    email: str
    password: str


@strawberry.type
class LoginType:
    """..."""

    email: str
    token: str


class AuthenticationService:
    """..."""

    pwd_contenxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    async def login(login_data: LoginInput):
        """..."""

        # check existing user in list_users.
        existing_user = next(
            (user for user in list_users if user["email"] == login_data.email),
            None)

        if not existing_user:
            raise ValueError("Email not found!")

        if not AuthenticationService.pwd_contenxt.verify(
            login_data.password, existing_user["password"]
        ):
            raise ValueError("Wrong Password!")

        token = JWTManager.generate_token({"sub": login_data.email})

        JWTManager.decode_jwt(token)

        return LoginType(email=login_data.email, token=token)

    @staticmethod
    async def register(user_data: RegisterInput):
        """..."""

        existing_user = next(
            (user for user in list_users if user["email"] == user_data.email),
            None)

        if existing_user:
            raise ValueError("Email is registered!")

        password = AuthenticationService.pwd_contenxt.hash(
            user_data.password)
        user = {
            "name": user_data.name,
            "email": user_data.email,
            "password": password
        }
        list_users.append(user)

        return "successfully registered data!"
