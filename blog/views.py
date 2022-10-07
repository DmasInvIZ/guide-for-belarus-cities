from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog_home.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


# @login_required
class BlogCreateView(CreateView):  # новое изменение
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView): # Новый класс
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
