from . import views
from django.conf.urls import url
app_name='blog'

urlpatterns=[
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^single/(\d+)/$',views.SingleView.as_view(),name='single')
]