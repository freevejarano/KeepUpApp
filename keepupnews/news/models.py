from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=1000)
    topic = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField()
    content = models.TextField()
