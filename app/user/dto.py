"""..."""
import strawberry


@strawberry.input
class UserCreateInput:
    """..."""
    name: str
    email: str
    password: str

