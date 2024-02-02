from django.db import models

# Create your models here.

# Category model
class Category(models.Model):
    name = models.CharField(max_length=30)

# Post model
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now_add = True)
    categories = models.ManyToManyField("Category", related_name = "posts")

    
