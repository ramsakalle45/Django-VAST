# myapp\models.py
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name    