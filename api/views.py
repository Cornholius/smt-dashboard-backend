from rest_framework.response import Response
from .models import Post, Tag, Media
from rest_framework import viewsets, permissions
from .serializers import PostSerializer, TagSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_date')
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        print('========== 1', request.FILES)
        write_serializer = PostSerializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)
        instance = write_serializer.save()
        read_serializer = PostSerializer(instance)
        for i in request.data['tags'].split():
            try:
                tag = Tag.objects.get(title=i)
                instance.tags.add(tag)
            except:
                new_tag = Tag.objects.create(title=i, slug=i)
                instance.tags.add(new_tag)
        if request.FILES:
            print('========== 2', request.FILES)
            print('========== 3', request.FILES['document'])
            print('========== 2', request.FILES)
            print('========== 2', request.FILES)

        return Response(read_serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('title')
    permission_classes = [permissions.AllowAny]
    serializer_class = TagSerializer
