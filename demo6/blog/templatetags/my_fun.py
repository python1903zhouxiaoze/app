from django.template import Library
from blog.models import *

register=Library()

@register.simple_tag
def newarticles():
    return Article.objects.all().order_by('-create_time')[:3]

@register.simple_tag
def gui():
    return Article.objects.dates('create_time','month')

@register.simple_tag
def category():
    return Category.objects.all()

@register.simple_tag
def tag():
    return Tag.objects.all()