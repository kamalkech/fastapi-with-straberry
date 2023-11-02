"""..."""

import typing

from starlette.requests import Request
from starlette.websockets import WebSocket
from strawberry.permission import BasePermission
from strawberry.types import Info

# local modules.
from app.auth.jwt_manager import JWTManager

# from app.service.authentication import list_users


class IsAuthenticated(BasePermission):
    """..."""

    message = "User is not Authenticated"

    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request: typing.Union[Request, WebSocket] = info.context["request"]

        # # Access headers authentication
        if "Authorization" in request.headers:
            request = info.context["request"]
            authorization = request.headers["authorization"]
            if authorization:
                token = authorization.split("Bearer ")[-1]
                result = JWTManager.verify_jwt(token)

                # payload = JWTManager.decode_jwt(token)
                # print("payload", payload.get('sub'))
                # email = payload.get('sub')
                # existing_user = next(
                #     (user for user in list_users if user["email"] == email))

                # if "admins" not in existing_user["roles"]:
                #     message = "User has not role permission"

                #     raise ValueError(message)

                return result

        return False
