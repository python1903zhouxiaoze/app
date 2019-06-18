from django.db import models

# Create your models here.


class Question(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Choice(models.Model):
    name=models.CharField(max_length=25)
    number=models.IntegerField(default=0)
    queid=models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.name