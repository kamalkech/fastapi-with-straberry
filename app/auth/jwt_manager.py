"""..."""

from typing import Optional
from datetime import datetime, timedelta
from jose import jwt

from app.config import Settings

# access to all env variables.
config = Settings()


class JWTManager:
    """..."""

    @staticmethod
    def generate_token(data: dict, expires_delta: Optional[timedelta] = None):
        """..."""

        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=float(config.ACCESS_TOKEN_EXPIRE_MINUTES)
            )

        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)

        return encode_jwt

    @staticmethod
    def verify_jwt(token: str):
        """..."""

        try:
            decode_token = jwt.decode(
                token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
            current_timestamp = datetime.utcnow().timestamp()

            if not decode_token:
                raise ValueError("Invalid token!")
            elif decode_token["exp"] <= current_timestamp:
                raise ValueError("Token expired!")
            return True
        except ValueError as error:
            print(error)
            return False

    @staticmethod
    def decode_jwt(token: str):
        """..."""

        return jwt.decode(
            token, config.SECRET_KEY, algorithms=[config.ALGORITHM])

