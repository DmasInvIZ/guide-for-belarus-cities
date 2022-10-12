from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body', 'date')
    search_fields = ('title', 'body')


admin.site.register(Post, PostAdmin)

