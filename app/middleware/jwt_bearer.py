"""..."""

import typing

from starlette.requests import Request
from starlette.websockets import WebSocket
from strawberry.permission import BasePermission
from strawberry.types import Info

from app.middleware.jwt_manager import JWTManager


class IsAuthenticated(BasePermission):
    """..."""

    message = "User is not Authenticated"

    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        # request = info.context["request"]
        # # Access headers authentication
        # authentication = request.headers["authentication"]
        # if authentication:
        #     token = authentication.split("Bearer ")[-1]
        #     return JWTManager.verify_jwt(token)
        request: typing.Union[Request, WebSocket] = info.context["request"]

        if "Authorization" in request.headers:
            request = info.context["request"]
            authorization = request.headers["authorization"]
            if authorization:
                token = authorization.split("Bearer ")[-1]
                result = JWTManager.verify_jwt(token)
                print("result", result)
                return result

        return False
