from django.contrib import admin
from .models import News, Towns, Districts, About

admin.site.register(Towns)
admin.site.register(Districts)
admin.site.register(About)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'news', 'date')
    search_fields = ['title']


admin.site.register(News, NewsAdmin)
