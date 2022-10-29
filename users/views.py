from msilib.schema import ListView

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import AuthUserForm, RegisterUserForm


# регистрация пользователя
class UserRegister(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = '/users/register'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'{username}, ваш аккаунт создан, вы можете войти')
        # form_valid = super().form_valid(form)
        # username = form.cleaned_data['username']
        # email = form.cleaned_data['email']
        # password1 = form.cleaned_data['password1']
        # password2 = form.cleaned_data['password2']
        # auth_user = authenticate(username=username, email=email, password1=password1, password2=password2)
        # login(self.request, auth_user)
        return super().form_valid(form)
        # return form_valid


# авторизация пользователей
class UserLogin(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = '/'


# class UserProfile(ListView):
#     pass


# # регистрация
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'{username}, Ваш аккаунт создан, можно войти на сайт.')
#             return redirect('/register')
#         else:
#             messages.warning(request, 'Что-то не так, проверьте, все ли поля заполнены правильно?')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'register.html', {'form': form})
#
#
# # страница профиля
@login_required
def user_profile_view(request):
    return render(request, 'profile.html')
