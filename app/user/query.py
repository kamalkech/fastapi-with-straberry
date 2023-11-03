"""..."""


from typing import List
import strawberry

from app.user.model import UserType
from app.user.service import UserService


@strawberry.type
class QueryUser:
    """..."""

    get_users: List[UserType] = strawberry.field(
        resolver=UserService.get_users
    )

    get_user_by_email: UserType = strawberry.field(
        resolver=UserService.get_user_by_email
    )
