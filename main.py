"""..."""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# strawberry.
import strawberry
from strawberry.fastapi import GraphQLRouter

# local modules.
from app.core.query import Query
from app.core.mutation import Mutation

app = FastAPI()

# accept sandbox apollo url.
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


# Health Check
@app.get("/health")
async def root():
    """..."""

    return {"message": "OK!"}

# GraphQL Schema and include prefix in router.
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter[object, object](schema)
app.include_router(graphql_app, prefix='/graphql')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3333)
