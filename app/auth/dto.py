"""..."""

import strawberry


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

