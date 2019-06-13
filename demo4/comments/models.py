from django.db import models

# Create your models here.
from blog.models import Article

class Comment(models.Model):
    #评论表和文章的关系：多对一
    name=models.CharField(max_length=50,verbose_name='名称')
    create_time=models.DateTimeField(auto_now=True)
    content=models.TextField(max_length=500,verbose_name='评论内容')
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    email=models.EmailField(blank=True,null=True,verbose_name='邮箱')
    url=models.URLField(blank=True,null=True,verbose_name='网址')


    def __str__(self):
        return self.name