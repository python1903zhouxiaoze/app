from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .admin import BookInfo,HeroInfo

def index(req):
    # return HttpResponse('这里是首页')

    # temp=loader.get_template('booktest/index.html')
    # res=temp.render({'username':'username','passwd':'**********'})
    # return HttpResponse(res)
    return render(req,'booktest/index.html',{'username':'username','passwd':'**********'})

def list(req):
    # return HttpResponse('这里是列表页')
    books=BookInfo.objects.all()
    # temp = loader.get_template('booktest/list.html')
    # res = temp.render({'books':books})
    # return HttpResponse(res)
    return render(req,'booktest/list.html',{'books':books})
def detail(req,id):
    # return HttpResponse('第%s个网页，%s'%(id,res))
    book=BookInfo.objects.get(pk=id)
    # temp = loader.get_template('booktest/detail.html')
    # res = temp.render({'book':book})
    # return HttpResponse(res)
    return render(req,'booktest/detail.html',{'book':book})


def deletehero(req,id):
    hero=HeroInfo.objects.get(pk=id)
    hero.delete()
    return HttpResponseRedirect('/detail/%s/'%(hero.book.id,))

def deletebook(req,id):
    book=BookInfo.objects.get(pk=id)
    book.delete()
    return HttpResponseRedirect('/list/')


#添加英雄
def addhero(req,id):
    book=BookInfo.objects.get(pk=id)
    if req.method=='GET':
        return render(req,'booktest/addhero.html',{'book':book})
    elif req.method=='POST':
        hero=HeroInfo()
        hero.name=req.POST.get('heroname')
        hero.content=req.POST.get('herocontent')
        hero.book=book
        hero.save()
        return HttpResponseRedirect('/detail/%s/'%(id,))