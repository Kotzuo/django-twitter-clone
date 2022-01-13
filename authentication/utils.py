import jwt
from accounts.models import User
from django.conf import settings
from django.shortcuts import get_object_or_404


def get_user_from_jwt_raw_token(raw_token) -> User:
    token = jwt.decode(
        raw_token,
        settings.SECRET_KEY,
        algorithms=settings.SIMPLE_JWT["ALGORITHM"]
    )

    return get_object_or_404(User, id=token["user_id"])
