from rest_framework import serializers
from .models import Post, Tag


class TagSerializer(serializers.ModelSerializer):

    ololo = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        # fields = ('id', 'title', 'slug')
        fields = '__all__'

    def get_ololo(self, instance):
        print('========', instance)
        tag = Tag.objects.filter(id=instance.id)
        # print(tag.id.all())
        return 'test'


class PostSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True, read_only=True)


    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'tags']

    def update(self, instance, validated_data):
        post = Post.objects.get(id=instance.id)
        for tag in validated_data['tags']:
            post.tags.add(Tag.objects.get(id=tag.id))
        return post
