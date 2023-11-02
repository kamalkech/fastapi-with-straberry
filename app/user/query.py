"""..."""
from typing import List
import strawberry

from app.user.resolver import get_users, get_user_by_email
from app.user.type import UserType


@strawberry.type
class QueryUser:
    """..."""
    get_users: List[UserType] = strawberry.field(resolver=get_users)
    # write get user by id here
    get_user_by_email: UserType = strawberry.field(resolver=get_user_by_email)
