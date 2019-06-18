from django.shortcuts import render

# Create your views here.
from .models import Question,Choice

#首页
def index(req):
    questions=Question.objects.all()
    return render(req,'toupiao/index.html',{'questions':questions})

def list(req,id):
    question=Question.objects.get(pk=id)
    return render(req,'toupiao/list.html',{'question':question})

def detail(req,id):
    people=Choice.objects.get(pk=id)
    people.number+=1
    people.save()
    question=people.queid
    return render(req,'toupiao/detail.html',{'question':question})