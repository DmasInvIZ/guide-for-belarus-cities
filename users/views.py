from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


# регистрация пользователей
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('/register')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
