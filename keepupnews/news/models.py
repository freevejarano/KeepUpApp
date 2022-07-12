from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    topic = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    content = models.TextField()
