"""..."""

import strawberry

from app.user.type import UserCreateInput, UserType
from app.user.resolver import create_user


@strawberry.type
class MutationUser:
    """..."""

    @strawberry.mutation
    def create_user(self, user_input: UserCreateInput) -> UserType:
        """..."""

        return create_user(user_input)
