from rest_framework import serializers
from .models import Post, Tag, Media


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True, read_only=True)
    media = MediaSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'tags', 'media']
        read_only_fields = ['document']