#自定义标签，在html文档中，有时候需要频繁的操作数据库，而且操作一样，
#这个时候我们不需要重复写，只需要写自定义标签即可


#引入自定义标签的模块
from django.template import Library

#引入Article类
from ..models import Article,Category,Tag

#注册，不加括号会报错 type object 'Library' has no attribute 'tags'
register=Library()

#加上装饰器
@register.simple_tag
def mytags(num=3):
    return Article.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def getarchieves():
    #dates第一个参数为处理字段，第二个参数为根据月来进行去重，显示所有不同的月份
    result=Article.objects.dates('create_time','month')
    return result

@register.simple_tag
def getcategorys():
    return Category.objects.all()

@register.simple_tag
def gettags():
    return Tag.objects.all()