from django.urls import path
from guide.views import ListObjectsView


urlpatterns = [
    path('', ListObjectsView.as_view()),
]
