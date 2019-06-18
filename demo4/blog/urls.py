from . import views
from django.conf.urls import url
from .feed import ArticleFeed
from haystack.views import SearchView

from django.views import static
from django.conf import settings

app_name='blog'

urlpatterns=[
    url(r'^$',views.IndexView.as_view(),name='index'),
    # url(r'^$',views.index,name='index'),
    url(r'^single/(\d+)/$',views.SingleView.as_view(),name='single'),
    url(r'^archieves/(\d+)/(\d+)/$',views.ArchieveView.as_view(),name='archieve'),
    url(r'^category/(\d+)/$',views.CategoryView.as_view(),name='category'),
    url(r'^tag/(\d+)/$',views.TagView.as_view(),name='tag'),
    url(r'^rss/$',ArticleFeed(),name='rss'),
    url(r'^contact/$',views.ContactView.as_view(),name='contact'),
    url(r'^search/$',SearchView(),name='search'),

    # url(r'^static/(?P<path>.*)$', static.serve,
    # {'document_root': settings.STATIC_ROOT}, name='static'),
]