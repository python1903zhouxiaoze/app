from django.shortcuts import render,get_object_or_404,redirect,reverse

# Create your views here.

from .models import *
from comments.forms import CommentForm
from django.http import HttpResponse
from comments.models import Comment
from django.core.paginator import Paginator
import markdown

#用视图类写
from django.views.generic import View


#提取公共方法
class Luyou:
    def aaa(self,req,articles):
        paginator = Paginator(articles, 1)
        pagenum = req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        return page



class IndexView(View):
    def get(self,req):
        # articles=Article.objects.all()
        articles=Article.objects.get_queryset().order_by('id')

        # from django.core.paginator import Paginator
        # 得到分页
        # paginator = Paginator(articles,2)
        # print(paginator.count)
        # print(paginator.object_list)
        # print(paginator.num_pages)
        # print(paginator.page_range)
        # # 得到页面
        # page = paginator.get_page(3)
        # print(page.object_list)
        # # 由页面得到分页    分页可以得到页面  页面可以得到分页

        # paginator=Paginator(articles,1)   #对从数据库中获得的所有文章进行分页

        # print(paginator.count)       #文章的个数
        # print(paginator.object_list)  #获取文章的列表，显示一个queryset列表，只显示标题
        # print(paginator.num_pages)    #一共有多少页
        # print(paginator.page_range)    #range(1,3)---1,2

        # pagenum=req.GET.get('page')
        # pagenum=1 if pagenum==None else pagenum
        #
        # page=paginator.get_page(pagenum)
        #
        # # page.path='/'
        # page.path=reverse('blog:index')
        #
        # return render(req,'blog/index.html',{'page':page})

        luyou=Luyou()
        page=luyou.aaa(req,articles)
        page.path = reverse('blog:index')
        return render(req,'blog/index.html',{'page':page})



class SingleView(View):
    def get(self,req,id):
        # article=Article.objects.get(pk=id)
        article=get_object_or_404(Article,pk=id)

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])#这里不加引号会报错

        article.body=md.convert(article.body)
        article.toc=md.toc

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

class ArchieveView(View):
    def get(self,req,year,month):
        # articles=Article.objects.filter(create_time__year=year,create_time__month=month)
        articles=Article.objects.get_queryset().order_by('id').filter(create_time__year=year,create_time__month=month)

        # paginator=Paginator(articles,1)
        # pagenum=req.GET.get('page')
        # pagenum=1 if pagenum==None else pagenum
        # page=paginator.get_page(pagenum)
        # # page.path='/archieve/%s/%s'%(year,month)
        # page.path=reverse('blog:archieve',args=(year,month))
        # return render(req,'blog/index.html',{'page':page})

        luyou = Luyou()
        page = luyou.aaa(req, articles)
        page.path = reverse('blog:archieve', args=(year, month))
        return render(req,'blog/index.html',{'page':page})



class CategoryView(View):
    def get(self,req,id):
        category=get_object_or_404(Category,pk=id)
        # articles=category.article_set.all()
        articles=category.article_set.get_queryset().order_by('id')


        # paginator = Paginator(articles, 1)
        # pagenum = req.GET.get('page')
        # pagenum = 1 if pagenum == None else pagenum
        # page = paginator.get_page(pagenum)
        # # page.path = '/category/%s' % (id)
        # page.path =reverse('blog:category',args=(id,))
        # return render(req,'blog/index.html',{'page':page})

        luyou = Luyou()
        page = luyou.aaa(req, articles)
        page.path =reverse('blog:category',args=(id,))
        return render(req,'blog/index.html',{'page':page})



class TagView(View):
    def get(self,req,id):
        tag=get_object_or_404(Tag,pk=id)
        # articles=tag.article_set.all()
        articles=tag.article_set.get_queryset().order_by('id')

        # paginator = Paginator(articles, 1)
        # pagenum = req.GET.get('page')
        # pagenum = 1 if pagenum == None else pagenum
        # page = paginator.get_page(pagenum)
        # # page.path = '/tag/%s' % (id)
        # page.path = reverse('blog:tag',args=(id,))
        # return render(req,'blog/index.html',{'page':page})

        luyou = Luyou()
        page=luyou.aaa(req,articles)
        page.path = reverse('blog:tag',args=(id,))
        return render(req,'blog/index.html',{'page':page})


