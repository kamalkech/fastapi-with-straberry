"""..."""

import strawberry

from app.user.model import UserType
from app.user.dto import UserCreateInput
from app.user.service import UserService


@strawberry.type
class MutationUser:
    """..."""

    @strawberry.mutation
    def create_user(self, user_input: UserCreateInput) -> UserType:
        """..."""

        return UserService.create_user(user_input)
