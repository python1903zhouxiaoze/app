from django.shortcuts import render,redirect,reverse

# Create your views here.

from django.views.generic import View
from django.http import HttpResponse
from .models import Question,Choice

#用装饰器装饰一下
def checklogin(func):
    def check(self,req,*args):
        #cookie写法
        # if req.COOKIES.get('username'):
        #session写法
        if req.session.get('username'):
            # print(req.COOKIES)  #{'username': 'admin'}
            # print(req.session)
            #<django.contrib.sessions.backends.db.SessionStore object at 0x000001F3BC874390>
            return func(self,req,*args)
        else:
            return redirect(reverse('toupiao:login'))
    return check

class Index(View):
    @checklogin
    def get(self,req):
        questions=Question.objects.all()
        return render(req,'toupiao/index.html',locals())


class List(View):
    @checklogin
    def get(self,req,id):
        question=Question.objects.get(pk=id)
        return render(req,'toupiao/list.html',locals())
    def post(self,req,id):
        c_id=req.POST.get('f')
        choice=Choice.objects.get(pk=c_id)
        choice.number+=1
        choice.save()
        return redirect(reverse('toupiao:detail',args=(id,)))

class Detail(View):
    @checklogin
    def get(self,req,id):
        question=Question.objects.get(pk=id)
        return render(req,'toupiao/detail.html',locals())
        # return HttpResponse('%s'%(question,))

class Login(View):
    def get(self,req):
        return render(req,'toupiao/login.html')
    def post(self,req):
        username=req.POST.get('username')
        passwd=req.POST.get('passwd')

        #cookie写法
        # res=redirect(reverse('toupiao:index'))
        # res.set_cookie('username',username)
        # return res

        #session写法
        req.session['username']=username
        return redirect(reverse('toupiao:index'))