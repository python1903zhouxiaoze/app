from django.contrib import admin

# Register your models here.

from .models import Tag,Category,Article,Ads,MessageInfo
#引入的分别是  标签表，分类表，文章表



admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Ads)
admin.site.register(MessageInfo)