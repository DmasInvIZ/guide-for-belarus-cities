from django.contrib import admin
from .models import News, Towns, Districts, About, UserTowns


class NewsAdmin(admin.ModelAdmin):
    """Новости"""
    list_display = ('title', 'author', 'news', 'date')
    search_fields = ('title', 'news')
    prepopulated_fields = {'slug': ('title',)}


class DistrictsAdmin(admin.ModelAdmin):
    """Области страны"""
    list_display = ('name', 'desk')
    search_fields = ('name', 'desk')
    prepopulated_fields = {'area_slug': ('name',)}


class TownsAdmin(admin.ModelAdmin):
    """Города"""
    list_display = ('name', 'district', 'short_info', 'watch', 'eat', 'sleep')
    search_fields = ('name',)
    prepopulated_fields = {'town_slug': ('name',)}


class AboutAdmin(admin.ModelAdmin):
    """Страница 'О проекте'"""
    list_display = ('post', 'date')
    search_fields = ('post',)


class UserTownsAdmin(admin.ModelAdmin):
    """Предложения публикаций от пользователей"""
    list_display = ('town', 'is_published')
    search_fields = ('town', 'watch', 'eat', 'sleep')
    list_editable = ('is_published',)
    list_filter = ('is_published',)


admin.site.register(News, NewsAdmin)
admin.site.register(Districts, DistrictsAdmin)
admin.site.register(Towns, TownsAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(UserTowns, UserTownsAdmin)
