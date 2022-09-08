from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from demo.filters import PostFilterSet
from demo.models import Post
from demo.permissions import IsPostOwner
from demo.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsPostOwner]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_fields = ['is_private', 'creator', 'updated_at']
    filterset_class = PostFilterSet
    search_fields = ['text', 'creator__username']

    def get_queryset(self):
        filter_params = Q(is_private=False)
        if self.request.user.is_authenticated:
            filter_params |= Q(creator=self.request.user)
        return Post.objects.filter(filter_params)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
