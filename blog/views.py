from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView  # новое изменение

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog_home.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_home.html'


class BlogCreateView(CreateView):  # новое изменение
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body']