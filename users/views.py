from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm


# регистрация
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, Ваш аккаунт создан, можно войти на сайт.')
            return redirect('/register')
        else:
            messages.warning(request, 'Что-то не так, проверьте, все ли поля заполнены правильно?')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


# страница профиля
@login_required
def profile(request):
    return render(request, 'profile.html')
