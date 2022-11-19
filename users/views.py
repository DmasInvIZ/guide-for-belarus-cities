from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from users.forms import AuthUserForm, RegisterUserForm, RegisterUserFormStep2


# регистрация пользователя
class UserRegister(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = '/users/register'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'{username}, ваш аккаунт создан, вы можете войти')
        return super().form_valid(form)


# авторизация пользователей
class UserLogin(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    # success_url = '/users/profile'


# после регистрации предлагается дополнить инфу о себе
class UserRegisterStep2(CreateView):
    model = User
    template_name = 'register_next.html'
    form_class = RegisterUserFormStep2
    success_url = '/users/login'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'{username}, ваш аккаунт создан, вы можете войти')
        return super().form_valid(form)


# страница профиля
@login_required
def user_profile_view(request):
    return render(request, 'profile.html')
