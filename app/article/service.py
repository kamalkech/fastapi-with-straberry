"""..."""

from typing import List
from app.article.model import ArticleType


class UserService:
    """..."""

    @staticmethod
    async def get_articles() -> List[ArticleType]:
        """..."""

        return [
            ArticleType(
                id=1,
                title="Hello",
                content="World"
            )
        ]
