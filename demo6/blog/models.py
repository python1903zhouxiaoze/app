from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Tag(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Category(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Article(models.Model):
    title=models.CharField(max_length=50)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    create_time=models.DateTimeField(auto_now=True)
    update_time=models.DateTimeField(auto_now_add=True)
    views=models.IntegerField(default=0)
    #外键分类表，和分类表一对多的关系
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    #外键标签表，和标签表多对多的关系
    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return self.title



