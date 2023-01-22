from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# регистрация пользователей
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Используйте простой логин')
    email = forms.EmailField(label='Адрес электронной почты', help_text='Используйте реальную почту')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


# авторизация пользователей
class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        username = forms.CharField(label='Логин', help_text='"подсказка логина"')

        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
