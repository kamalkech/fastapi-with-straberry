"""..."""

from passlib.context import CryptContext

from app.auth.jwt_manager import JWTManager
from app.auth.model import LoginType
from app.auth.dto import (
    RegisterInput,
    LoginInput,
)


hash_pass = CryptContext(schemes=["bcrypt"], deprecated="auto")
list_users = [
    {
        "name": "root",
        "email": "root@email.com",
        "password": hash_pass.hash("root"),
        "roles": ["admin", "user"]
    },
    {
        "name": "morocco",
        "email": "morocco@email.com",
        "password": hash_pass.hash("morocco"),
        "roles": ["user"]
    }
]


class AuthenticationService:
    """..."""

    pwd_contenxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    async def login(login_data: LoginInput) -> LoginType:
        """..."""

        # check existing user in list_users.
        existing_user = next(
            (user for user in list_users if user["email"] == login_data.email),
            None)

        if not existing_user:
            raise ValueError("Email not found!")

        stored_password = existing_user.get("password")

        if not stored_password or not isinstance(
            stored_password, (str, bytes)
        ):
            raise ValueError("Invalid password format!")

        if not AuthenticationService.pwd_contenxt.verify(
            login_data.password, stored_password
        ):
            raise ValueError("Wrong Password!")

        # token = JWTManager.generate_token({"sub": login_data.email})
        token = JWTManager.generate_token(
            {"sub": login_data.email})

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
            "password": password,
            "roles": ["user"]
        }
        list_users.append(user)

        return "successfully registered data!"

