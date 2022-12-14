from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guide.urls')),
    path('users/', include('users.urls')),
    path('blog/', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
