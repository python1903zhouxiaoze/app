from django.db import models

# Create your models here.
from django.contrib.auth.models import User

#标签表，和文章表多对多
class Tag(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

#分类表，和文章表一对多
class Category(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

#文章表
class Article(models.Model):
    title=models.CharField(max_length=50)
    #User的外键
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    create_time=models.DateTimeField(auto_now=True)
    update_time=models.DateTimeField(auto_now_add=True)
    views=models.IntegerField(default=0)
    #分类表的外键
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    #标签表的外键
    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
