from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

class Category(models.Model):
    categoryName = models.CharField(max_length=64, unique=True)

class Post(models.Model):
    pass

class PostCategory(models.Model):
    pass

class Comment(models.Model):
    pass