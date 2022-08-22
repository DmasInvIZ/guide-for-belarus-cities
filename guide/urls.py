from django.urls import path
from guide.views import ListObjectsView, about_view

urlpatterns = [
    path('', ListObjectsView.as_view()),
    path('about.html/', about_view),
]
