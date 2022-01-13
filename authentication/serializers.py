from accounts.serializers import AccountSerializer
from django.conf import settings
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UserTokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if settings.SIMPLE_JWT["UPDATE_LAST_LOGIN"]:
            update_last_login(None, self.user)

        return {"user": AccountSerializer(self.user).data, "token": data}
