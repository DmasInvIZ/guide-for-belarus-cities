from django.urls import path
from .views import *  # BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView


urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),  # удаление поста
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),  # изменить пост
    path('blog/new_post/', BlogCreateView.as_view(), name='new_post'),  # новый пост
    # path('blog/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),  # детали поста
    path('blog/', BlogListView.as_view(), name='blog_home'),  # страница с постами
]
