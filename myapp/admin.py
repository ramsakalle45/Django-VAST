# myapp\admin.py
from django.contrib import admin
from .models import Post, Item

admin.site.register(Post)
admin.site.register(Item)