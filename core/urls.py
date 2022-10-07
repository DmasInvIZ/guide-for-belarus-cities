from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guide.urls')),
    path('', include('users.urls')),
    path('', include('blog.urls')),
]
