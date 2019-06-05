from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.

class HeroInfoInlines(admin.StackedInline):
    model=HeroInfo
    extra = 1

class BookInfoAdmin(admin.ModelAdmin):
    #重写list_display，让后台显示哪些字段
    list_display = ('title','pub_date')
    list_filter = ('title',)
    list_per_page = 20
    inlines = [HeroInfoInlines]
    search_fields = ('title',)
#在注册模型时，注册该模型的后台管理类，通过管理类重写后台
admin.site.register(BookInfo,BookInfoAdmin)

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ('name','content')
    list_filter = ('name',)
    search_fields = ('name','content')

admin.site.register(HeroInfo,HeroInfoAdmin)


