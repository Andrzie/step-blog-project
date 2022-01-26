from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    username = models.CharField(max_length=15)
    text = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.username



















# Create your models here.
