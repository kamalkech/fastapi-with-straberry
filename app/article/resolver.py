"""..."""
from typing import List
from strawberry.types import Info
from app.article.type import ArticleType


def get_articles(info: Info) -> List[ArticleType]:
    """..."""
    return [
        ArticleType(
            id=1,
            title="Hello",
            content="World"
        )
    ]
