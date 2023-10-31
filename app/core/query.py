"""..."""
from strawberry.tools import merge_types

from app.article.query import QueryArticle
from app.user.query import QueryUser

queries = (QueryArticle, QueryUser)
Query = merge_types("Query", queries)
