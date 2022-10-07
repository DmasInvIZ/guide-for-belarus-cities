from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView

urlpatterns = [
    path('blog/new_post/', BlogCreateView.as_view(), name='new_post'),  # новый пост
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('blog/', BlogListView.as_view(), name='blog_home'),
]
