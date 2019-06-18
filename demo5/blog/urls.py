from django.conf.urls import url
from .views import *
from .feed import ArticleFeed
app_name='blog'

urlpatterns=[
    url('^$',IndexView.as_view(),name='index'),
    url('^single/(\d+)/$',SingleView.as_view(),name='single'),
    url('^gui/(\d+)/(\d+)/$',Gui.as_view(),name='gui'),
    url('^category/(\d+)/$',CategoryView.as_view(),name='category'),
    url('^tag/(\d+)/$',TagView.as_view(),name='tag'),
    url('^rss1/$',ArticleFeed(),name='rss'),
]