from .models import Post, Tag
from rest_framework import viewsets, permissions
from .serializers import PostSerializer, TagSerializer


# Todo ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_date')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('title')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TagSerializer
