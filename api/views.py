from os import name
from rest_framework.response import Response
from .models import Post, Tag, Media
from rest_framework import viewsets, permissions
from .serializers import PostSerializer, TagSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_date')
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
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
            for file in request.FILES.getlist('document'):
                instance.media.create(document=file, name=file.name)
                print(instance.media)

        return Response(read_serializer.data)



class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('title')
    permission_classes = [permissions.AllowAny]
    serializer_class = TagSerializer
