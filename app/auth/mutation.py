"""."""
import strawberry

# local modules.
from app.auth.jwt_bearer import IsAuthenticated
from app.auth.model import LoginType
from app.auth.dto import LoginInput
from app.auth.service import AuthenticationService


@strawberry.type
class MutationAuth:
    """..."""

    @strawberry.mutation
    async def login(self, login_data: LoginInput) -> LoginType:
        """..."""
        return await AuthenticationService.login(login_data)

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    def for_member(self, name: str) -> str:
        """..."""
        return f"For member {name}"
