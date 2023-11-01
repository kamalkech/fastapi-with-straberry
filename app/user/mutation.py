"""."""
import strawberry

from app.user.type import UserCreateInput, UserType
from app.user.resolver import create_user
from app.middleware.jwt_bearer import IsAuthenticated

from app.Service.authentication import (
    AuthenticationService,
    LoginInput,
    LoginType
)


@strawberry.type
class MutationUser:
    """..."""
    @strawberry.mutation
    def create_user(self, user_input: UserCreateInput) -> UserType:
        """..."""
        return create_user(user_input)

    @strawberry.mutation
    async def login(self, login_data: LoginInput) -> LoginType:
        """..."""
        return await AuthenticationService.login(login_data)

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    def for_member(self, name: str) -> str:
        """..."""
        return f"For member {name}"
