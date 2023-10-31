"""..."""
from typing import List
import strawberry

from app.article.resolver import get_articles
from app.article.type import ArticleType


@strawberry.type
class QueryArticle:
    """..."""
    get_articles: List[ArticleType] = strawberry.field(resolver=get_articles)
