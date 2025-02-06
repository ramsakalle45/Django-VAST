# myapp\models.py
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    published_date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.title, self.content
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name    
    
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
