from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse

class ArticleFeed(Feed):
    title='小泽博客'
    description='django小知识'
    link='/'

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body[:20]

    def item_link(self, item):
        return reverse('blog:single',args=(item.id,))
