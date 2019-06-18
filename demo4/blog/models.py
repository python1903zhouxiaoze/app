from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from tinymce.models import HTMLField


#标签表
class Tag(models.Model):
    #和文章表之间的关系：多对多
    #标签名
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

#分类表
class Category(models.Model):
    #和文章之间的关系：一对多
    #类名
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

#文章表
class Article(models.Model):
    #文章标题
    title=models.CharField(max_length=50)
    #作者
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    #内容，比较多，使用textfield
    body=models.TextField()
    #创建时间，自动填充
    create_time=models.DateTimeField(auto_now=True)
    #更新时间
    update_tiem=models.DateTimeField(auto_now_add=True)
    #浏览数
    views=models.IntegerField(default=0)
    #分类表
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    h=models.ManyToManyField(Tag)


    def __str__(self):
        return self.title


class Ads(models.Model):
    pic=models.ImageField(upload_to='ads')
    desc=models.CharField(max_length=20)
    url=models.CharField(max_length=20)

    def __str__(self):
        return self.desc


class MessageInfo(models.Model):
    email=models.EmailField()
    info=HTMLField()

    def __str__(self):
        return self.email


