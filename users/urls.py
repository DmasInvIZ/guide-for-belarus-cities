from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from users.views import UserLogin, UserRegister, user_profile_view

urlpatterns = [
    path('register/', UserRegister.as_view(template_name='register.html'), name='register'),
    path('profile/', user_profile_view, name='profile'),
    path('login/', UserLogin.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('please_login/', LoginView.as_view(template_name='please_login.html'), name='please_login'),
    path('register_next/', UserRegister.as_view(template_name='register_next.html'), name='register_next'),
]
