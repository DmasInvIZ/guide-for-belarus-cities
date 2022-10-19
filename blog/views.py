from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
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


# def profile(request):
#     global current_user
#     current_user = request.user
#     return render(request, 'profile.html', {'current_user': current_user})


# создание нового поста
@method_decorator(login_required, name='dispatch')  # только для авторизованных
class BlogCreateView(CreateView):
    model = Post
    template_name = 'new_post.html'

    def get_author(self):
        author = self.request.user
        return author

    fields = ['title', 'author', 'body']  # поля формы


# редактирование поста
@method_decorator(login_required, name='dispatch')  # только для авторизованных
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']  # поля формы


# удаление поста
@method_decorator(login_required, name='dispatch')  # только для авторизованных
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog_home')


