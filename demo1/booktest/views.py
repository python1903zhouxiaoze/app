from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import loader
from .admin import BookInfo,HeroInfo

def index(req):
    # return HttpResponse('这里是首页')

    temp=loader.get_template('booktest/index.html')
    res=temp.render({'username':'username','passwd':'**********'})
    return HttpResponse(res)

def list(req):
    # return HttpResponse('这里是列表页')
    books=BookInfo.objects.all()
    temp = loader.get_template('booktest/list.html')
    res = temp.render({'books':books})
    return HttpResponse(res)

def detail(req,id):
    # return HttpResponse('第%s个网页，%s'%(id,res))
    book=BookInfo.objects.get(pk=id)
    temp = loader.get_template('booktest/detail.html')
    res = temp.render({'book':book})
    return HttpResponse(res)