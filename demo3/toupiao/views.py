from django.shortcuts import render,redirect,reverse

# Create your views here.

from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import Question,Choice
from .forms import LoginForm,MyUserLoginForm,MyUserRegisterForm
from django.contrib.auth import authenticate,login,logout
from .models import MyUser
from django.core.mail import send_mail,EmailMultiAlternatives
from itsdangerous import TimedJSONWebSignatureSerializer

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

        # from django.conf import settings
        # mail=EmailMultiAlternatives('测试邮件','<h1><a href="www.baidu.com">百度</a><h1>',settings.DEFAULT_FROM_EMAIL,['email'])
        # mail.content_subtype='html'
        # mail.send()


        return render(req,'toupiao/login.html',locals())
    def post(self,req):
        username=req.POST.get('username')
        password=req.POST.get('password')
        verify=req.POST.get('id_verify')
        #cookie写法
        # res=redirect(reverse('toupiao:index'))
        # res.set_cookie('username',username)
        # return res

        #session写法
        # req.session['username']=username
        # return redirect(reverse('toupiao:index'))

        #使用django自带授权系统，如果授权成功，返回user

        # user=authenticate(req,username=username,password=password)
        # if user:
        #     login(req,user)
        #     return redirect(reverse('toupiao:index'))

        user = MyUser.objects.filter(username=username).first()
        if user:
            if user.check_password(password):
                # user1 = authenticate(req, username=username, password=password)
                if user.is_active:
                    # if verify == req.session.get('verifycode'):
                    from django.core.cache import cache
                    if verify == cache.get('verifycode'):
                        user1=authenticate(req,username=username,password=password)
                        login(req, user1)
                        return redirect(reverse('toupiao:index'))
                    else:
                        lf = MyUserLoginForm()
                        errormessage = '验证码错误'
                        return render(req, 'toupiao/login.html', locals())
                else:
                    lf = MyUserLoginForm()
                    errormessage = '账号未激活'
                    return render(req,'toupiao/login.html',locals())
            else:
                lf = MyUserLoginForm()
                errormessage = '密码不正确'
                return render(req,'toupiao/login.html',locals())
        else:
            lf = MyUserLoginForm()
            errormessage = '用户名不存在'
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
            # print(username,password,email)
            # user=MyUser.objects.create_user(username=username,email=email,password=password)
            # return redirect(reverse('toupiao:index'))
            user=MyUser.objects.create_user(username=username,email=email,password=password)
            user.is_active=False
            user.save()

            from django.conf import settings
            userid = user.id
            util=TimedJSONWebSignatureSerializer(secret_key=settings.SECRET_KEY)
            userid=util.dumps({'userid':userid}).decode('utf-8')


            info='<a href="http://127.0.0.1:8000/active/%s/">点击激活</a>'%(userid,)
            from django.conf import settings
            mail=EmailMultiAlternatives('请激活',info,from_email=settings.DEFAULT_FROM_EMAIL,to=['18339955260@163.com'])
            mail.content_subtype='html'
            mail.send()

            if user:
                return redirect(reverse("toupiao:login"))
        except:
            lf=MyUserLoginForm()
            errormessage1='注册失败...'
            return render(req,'toupiao/login.html',locals())


class LogOut(View):
    def get(self,req):
        logout(req)
        return redirect(reverse('toupiao:login'))

class Active(View):
    def get(self,req,id):
        from django.conf import settings
        util=TimedJSONWebSignatureSerializer(secret_key=settings.SECRET_KEY)
        #这里是loads，否则会出错，写load不对
        obj=util.loads(id)
        newid=obj['userid']
        user=MyUser.objects.filter(pk=newid).first()
        if user:
            user.is_active=True
            user.save()
            return redirect(reverse('toupiao:login'))

class CheckUserName(View):
    def get(self,req):
        username=req.GET.get('username')
        user=MyUser.objects.filter(username=username).first()
        if user:
            return JsonResponse({'statecode':'1'})
        else:
            return JsonResponse({'statecode':'0','error':'用户名不存在'})

import random
from PIL import Image,ImageDraw,ImageFont
import io
class VerfiyView(View):
    def get(self,req):
        # 定义变量，用于画面的背景色、宽、高
        bgcolor = (random.randrange(20, 100),
                   random.randrange(20, 100),
                   random.randrange(20, 100))
        width = 100
        heigth = 25
        # 创建画面对象
        im = Image.new('RGB', (width, heigth), bgcolor)
        # 创建画笔对象
        draw = ImageDraw.Draw(im)
        # 调用画笔的point()函数绘制噪点
        for i in range(0, 100):
            xy = (random.randrange(0, width), random.randrange(0, heigth))
            fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
            draw.point(xy, fill=fill)
        # 定义验证码的备选值
        str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
        # 随机选取4个值作为验证码
        rand_str = ''
        for i in range(0, 4):
            rand_str += str1[random.randrange(0, len(str1))]
        # 构造字体对象
        font = ImageFont.truetype('calibri.ttf', 23)
        fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
        # 绘制4个字
        draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
        draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
        draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
        draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
        # 释放画笔
        del draw
        # req.session['verifycode'] = rand_str

        from django.core.cache import cache
        cache.set('verifycode',rand_str)

        f = io.BytesIO()
        im.save(f, 'png')
        # 将内存中的图片数据返回给客户端，MIME类型为图片png
        return HttpResponse(f.getvalue(), 'image/png')


#发送测试邮件
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
class SendMail(View):
    def get(self,req):
        try:
            #普通的发送邮件
            # send_mail('测试邮件','<h1>正文</h1>',settings.DEFAULT_FROM_EMAIL,['18339955260@163.com'])

            #新写法，可以发送HTML格式
            mail=EmailMultiAlternatives(subject='新格式邮件',body='<h1><a href="http://www.baidu.com">百度</a></h1>',from_email=settings.DEFAULT_FROM_EMAIL,to=['18339955260@163.com'])
            mail.content_subtype='html'
            mail.send()

            return HttpResponse('发送成功')
        except:
            return HttpResponse('发送失败')
