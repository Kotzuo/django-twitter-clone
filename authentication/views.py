from accounts.serializers import AccountSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .serializers import UserTokenObtainPairSerializer
from .utils import get_user_from_jwt_raw_token


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer


class UserTokenRefreshView(TokenRefreshView):
    def post(self, request):
        token_serializer = self.serializer_class(data=request.data)
        try:
            token_serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        user = get_user_from_jwt_raw_token(request.data["refresh"])
        user_serializer = AccountSerializer(user)

        return Response({'user': user_serializer.data, 'token': token_serializer.validated_data}, status=status.HTTP_200_OK)
