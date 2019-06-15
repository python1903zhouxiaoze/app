from django.contrib.syndication.views import Feed
from .models import Article

class ArticleFeed(Feed):
    title='周晓泽的个人博客'
    description='介绍一些django项目开发的小知识点'
    link='/'

    def items(self):
        return Article.objects.all().order_by('-create_time')[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body[:10]

    def item_link(self, item):
        return '/single/%s'%(item.id,)




