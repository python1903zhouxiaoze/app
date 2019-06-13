from django.shortcuts import render,get_object_or_404,redirect,reverse

# Create your views here.

from .models import *
from comments.forms import CommentForm
from django.http import HttpResponse
from comments.models import Comment

#用视图类写
from django.views.generic import View

class IndexView(View):
    def get(self,req):
        articles=Article.objects.all()
        return render(req,'blog/index.html',locals())

class SingleView(View):
    def get(self,req,id):
        # article=Article.objects.get(pk=id)
        article=get_object_or_404(Article,pk=id)
        cf=CommentForm()
        return render(req,'blog/single.html',locals())
    def post(self,req,id):
        # name=req.POST.get('name')
        # email=req.POST.get('email')
        # url=req.POST.get('url')
        # content=req.POST.get('content')

        cf=CommentForm(req.POST)
        print(cf)
        if cf.is_valid():
            res=cf.save(commit=False)
            res.article=get_object_or_404(Article,pk=id)
            res.save()
            return redirect(reverse('blog:single',args=(id,)))
