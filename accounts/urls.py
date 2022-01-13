from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .views import AccountViewSet

app_name = "accounts"


router = routers.DefaultRouter()
router.register('', AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
