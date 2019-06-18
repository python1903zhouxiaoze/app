from django.contrib.syndication.views import Feed
from django.shortcuts import reverse
from .models import Article

class ArticleFeed(Feed):
    title='周'
    description='周的博客'
    link='/'

    def items(self):
        return Article.objects.all().order_by('-create_time')[:3]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.body[:30]
    def item_link(self, item):
        return reverse('blog:single',args=(item.id,))
