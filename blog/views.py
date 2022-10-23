from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.utils.decorators import method_decorator  # только для авторизованных
from .models import Post

from django.contrib import messages


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
    fields = ['title', 'body']  # поля формы

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        messages.success(self.request, f'Запись создана')
        return super().form_valid(form)


# редактирование поста
@method_decorator(login_required, name='dispatch')  # только для авторизованных
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    permission_required = 'auth.change_user'
    template_name = 'post_edit.html'
    fields = ['title', 'body']  # поля формы

    def form_valid(self, form):
        messages.success(self.request, f'Запись изменена')
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
            # return HttpResponse('Вы не можете этого сделать...')
        return kwargs


# удаление поста
@method_decorator(login_required, name='dispatch')  # только для авторизованных
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog_home')

    def post(self, request, *args, **kwargs):
        return super().post(request)

    def form_valid(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, f'Запись удалена')
        if self.request.user != self.object.author:
            # return self.handle_no_permission()
            return HttpResponse('Вы не можете этого сделать...')
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
