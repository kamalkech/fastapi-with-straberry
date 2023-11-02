"""..."""

import strawberry
from app.user.mutation import MutationUser
from app.auth.mutation import MutationAuth


@strawberry.type
class Mutation(MutationUser, MutationAuth):
    """..."""
