from django.shortcuts import render,redirect,reverse

# Create your views here.

from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import Question,Choice
from .forms import LoginForm,MyUserLoginForm,MyUserRegisterForm
from django.contrib.auth import authenticate,login,logout
from .models import MyUser

#用装饰器装饰一下
def checklogin(func):
    def check(self,req,*args):
        #cookie写法
        # if req.COOKIES.get('username'):
        #session写法
        # if req.session.get('username'):
        if req.user and req.user.is_authenticated:
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
        user=req.user
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
        lf=MyUserLoginForm()
        rf=MyUserRegisterForm()
        return render(req,'toupiao/login.html',locals())
    def post(self,req):
        username=req.POST.get('username')
        password=req.POST.get('password')

        #cookie写法
        # res=redirect(reverse('toupiao:index'))
        # res.set_cookie('username',username)
        # return res

        #session写法
        # req.session['username']=username
        # return redirect(reverse('toupiao:index'))

        #使用django自带授权系统，如果授权成功，返回user

        user=authenticate(req,username=username,password=password)
        if user:
            login(req,user)
            return redirect(reverse('toupiao:index'))

        else:
            lf=MyUserLoginForm()
            errormessage='账号或密码错误'
            return render(req,'toupiao/login.html',locals())

class Register(View):
    def get(self,req):
        rf=MyUserRegisterForm()
        return render(req,'toupiao/register.html',locals())
    def post(self,req):
        try:
            username=req.POST.get('username')
            password=req.POST.get('password')
            email=req.POST.get('email')
            print(username,password,email)
            user=MyUser.objects.create_user(username=username,email=email,password=password)
            if user:
                return redirect(reverse('toupiao:login'))
        except:
            lf=MyUserLoginForm()
            errormessage1='注册失败...'
            return render(req,'toupiao/login.html',locals())


class LogOut(View):
    def get(self,req):
        logout(req)
        return redirect(reverse('toupiao:login'))


