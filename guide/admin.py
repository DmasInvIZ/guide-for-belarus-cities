from django.contrib import admin
from .models import News, Towns, Districts, About


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'news', 'date')
    search_fields = ('title', 'news')


class DistrictsAdmin(admin.ModelAdmin):
    list_display = ('name', 'desk')
    search_fields = ('name', 'desk')


class TownsAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'short_info', 'full_desk')
    search_fields = ('name', 'full_desk')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('post', 'date')
    search_fields = ('post',)


admin.site.register(News, NewsAdmin)
admin.site.register(Districts, DistrictsAdmin)
admin.site.register(Towns, TownsAdmin)
admin.site.register(About, AboutAdmin)
