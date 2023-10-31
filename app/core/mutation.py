"""..."""

import strawberry
from app.user.mutation import MutationUser


@strawberry.type
class Mutation(MutationUser):
    """..."""
