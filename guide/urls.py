from django.urls import path
from guide.views import ListObjectsView, about_view, what_to_watch_view

urlpatterns = [
    path('', ListObjectsView.as_view()),
    path('about/', about_view),
    path('what-to-watch.html/', what_to_watch_view)
]
