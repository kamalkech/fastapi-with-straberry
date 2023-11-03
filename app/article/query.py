"""..."""

from typing import List
import strawberry

from app.article.service import UserService
from app.article.model import ArticleType


@strawberry.type
class QueryArticle:
    """..."""

    get_articles: List[ArticleType] = strawberry.field(
        resolver=UserService.get_articles)
