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
    weather = models.CharField(max_length=3)
# Create your models here.
