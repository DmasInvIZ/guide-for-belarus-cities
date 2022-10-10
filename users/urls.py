from django.contrib.auth import views as auth_views
from django.urls import path
from users import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('please_login/', auth_views.LoginView.as_view(template_name='please_login.html'), name='please_login'),
]