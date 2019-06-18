from django.shortcuts import render,redirect,reverse,get_object_or_404

# Create your views here.
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .form import CommentForms
from django.core.paginator import Paginator
import markdown

class Fenye:
    def aaa(self,req,articles):
        paginator = Paginator(articles, 1)
        pagenum = req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        return page


#首页视图类
class IndexView(View):
    def get(self,req):
        articles=Article.objects.all()

        f=Fenye()
        page=f.aaa(req,articles)
        page.path=reverse('blog:index')

        return render(req,'blog/index.html',{'page':page})


#single视图类
class SingleView(View):
    def get(self,req,id):
        article=get_object_or_404(Article,pk=id)
        cf=CommentForms()

        md=markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ])
        article.body=md.convert(article.body)
        article.toc=md.toc

        return render(req,'blog/single.html',locals())
    def post(self,req,id):
        artile=get_object_or_404(Article,pk=id)
        cf=CommentForms(req.POST)
        if cf.is_valid():
            res=cf.save(commit=False)
            res.article=artile
            res.save()
        return redirect(reverse('blog:single',args=(id,)))

#归档的视图类
class Gui(View):
    def get(self,req,year,month):
        articles=Article.objects.filter(create_time__year=year,create_time__month=month)

        f=Fenye()
        page=f.aaa(req,articles)
        page.path=reverse('blog:gui',args=(year,month))

        return render(req,'blog/index.html',{'page':page})


#分类的视图类
class CategoryView(View):
    def get(self,req,id):
        category=get_object_or_404(Category,pk=id)
        articles=category.article_set.all()

        f=Fenye()
        page=f.aaa(req,articles)
        page.path=reverse('blog:category',args=(id,))

        return render(req,'blog/index.html',locals())


#标签云视图类
class TagView(View):
    def get(self,req,id):
        tag=get_object_or_404(Tag,pk=id)
        articles=tag.article_set.all()

        f = Fenye()
        page = f.aaa(req, articles)
        page.path = reverse('blog:tag', args=(id,))

        return render(req,'blog/index.html',locals())



