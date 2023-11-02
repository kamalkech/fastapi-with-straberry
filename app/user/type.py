"""..."""
import strawberry


@strawberry.type
class UserType:
    """..."""
    name: str
    email: str
    password: str


@strawberry.input
class UserCreateInput:
    """..."""
    name: str
    email: str
    password: str
