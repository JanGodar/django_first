from django.db import models

# Create your models here.
class FirstApp(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_create = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)