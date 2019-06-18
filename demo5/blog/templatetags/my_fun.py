from django.template import Library
from blog.models import *

register=Library()

#最新文章
@register.simple_tag
def newarticles():
    return Article.objects.all().order_by('-create_time')[:3]


#自定义显示时间
@register.simple_tag
def time():
    #dates第一个参数：处理字段，第二个参数：按月显示，自动去重
    return Article.objects.dates('create_time','month')


#所有分类
@register.simple_tag
def category():
    return Category.objects.all()

#标签云
@register.simple_tag
def tag():
    return Tag.objects.all()
