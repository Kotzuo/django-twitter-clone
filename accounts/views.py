from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .permissions import AccountViewSetPermission
from .serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = [AccountViewSetPermission]
    serializer_class = AccountSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['get'])
    def me(self, request):
        return Response(AccountSerializer(request.user).data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def follow(self, request, pk=None):
        user = self.get_object()
        request.user.following.add(user)
        return Response({'status': 'ok'})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unfollow(self, request, pk=None):
        user = self.get_object()
        request.user.following.remove(user)
        return Response({'status': 'ok'})
