from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import *

urlpatterns = [
    path('register/', UserRegister.as_view(template_name='register.html'), name='register'),
    path('profile/', user_profile_view,  name='profile'),
    path('login/', UserLogin.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('please_login/', LoginView.as_view(template_name='please_login.html'), name='please_login'),
]
