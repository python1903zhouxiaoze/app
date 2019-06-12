from django.conf.urls import url
from .views import Index,List,Detail,Login,Register,LogOut

app_name='toupiao'

urlpatterns=[
    url(r'^$',Index.as_view(),name='index'),
    url(r'^list/(\d+)/$',List.as_view(),name='list'),
    url(r'^detail/(\d+)/$',Detail.as_view(),name='detail'),
    url(r'^login/$',Login.as_view(),name='login'),
    url(r'^register/',Register.as_view(),name='register'),
    url(r'^logout/$',LogOut.as_view(),name='logout'),
]