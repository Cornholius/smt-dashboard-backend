from django.conf import settings
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    document = models.FileField(blank=True)

    def __str__(self):
        return self.title


class Media(models.Model):
    document = models.FileField(blank=True)
    name = models.CharField(max_length=100, default='')
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE)

    def __str__(self):
        return self.document