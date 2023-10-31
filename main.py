"""..."""
import strawberry
from strawberry.fastapi import GraphQLRouter

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.query import Query
from app.core.mutation import Mutation


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()

origins = [
    "https://studio.apollographql.com",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """..."""
    return {"message": "Hello World!"}

app.include_router(graphql_app, prefix='/graphql')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3333)
