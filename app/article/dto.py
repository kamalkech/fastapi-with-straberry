"""..."""

import strawberry


@strawberry.input
class ArticleCreateInput:
    """..."""

    id: int
    title: str
    content: str

