from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .permissions import OnlyOwner
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, OnlyOwner]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.action == 'list':
            queryset = queryset.exclude(owner=self.request.user)

        if self.request.query_params.get('following') == 'true':
            queryset = queryset.filter(
                owner__in=self.request.user.following.all()
            )

        return queryset
