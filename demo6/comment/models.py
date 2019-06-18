from django.db import models

# Create your models here.
from blog.models import Article

class Comment(models.Model):
    name=models.CharField(max_length=50,verbose_name='名字：')
    content=models.TextField(max_length=500,verbose_name='评论：')
    email=models.EmailField(blank=True,null=True,verbose_name='邮箱：')
    url=models.URLField(blank=True,null=True,verbose_name='网址：')
    create_time=models.DateTimeField(auto_now=True)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)

