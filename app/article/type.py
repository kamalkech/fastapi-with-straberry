"""..."""

import strawberry


@strawberry.type
class ArticleType:
    """..."""

    id: int
    title: str
    content: str


@strawberry.input
class ArticleCreateInput:
    """..."""

    id: int
    title: str
    content: str
