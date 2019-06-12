from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Question(models.Model):
    title=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Choice(models.Model):
    title=models.CharField(max_length=50)
    number=models.IntegerField(default=0)
    queid=models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class MyUser(User):
    telephone=models.CharField(max_length=11)



