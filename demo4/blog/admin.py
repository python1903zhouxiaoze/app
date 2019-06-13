from django.contrib import admin

# Register your models here.

from .models import Tag,Category,Article
#引入的分别是  标签表，分类表，文章表


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)