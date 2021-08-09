from django.conf import settings
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, blank=True)
    # published_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    document = models.FileField(blank=True)
    # image = models.ImageField(blank=True, upload_to='images/')
    #
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title


class Media(models.Model):
    document = models.FileField(blank=True)
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE)


