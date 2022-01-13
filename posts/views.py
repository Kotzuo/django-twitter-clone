from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .filters import FollowingOnlyFilterBackend
from .models import Post
from .permissions import OnlyOwner
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, OnlyOwner]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [FollowingOnlyFilterBackend]

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.action == 'list':
            queryset = queryset.exclude(owner=self.request.user)

        return queryset
