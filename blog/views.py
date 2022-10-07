from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.utils.decorators import method_decorator  # только для авторизованных
from .models import Post


# выводит список постов
class BlogListView(ListView):
    model = Post
    template_name = 'blog_home.html'
    context_object_name = 'posts'
    ordering = '-date'  # сортировка постов по дате создания


# детали поста
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


# создание нового поста
@method_decorator(login_required, name='dispatch')  # только для авторизованных
class BlogCreateView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body']


# редактирование поста
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


# удаление поста
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog_home')