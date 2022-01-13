from django.urls import path

from .views import UserTokenObtainPairView, UserTokenRefreshView

app_name = "authentication"

urlpatterns = [
    path('token/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', UserTokenRefreshView.as_view(), name='token_refresh'),
]
