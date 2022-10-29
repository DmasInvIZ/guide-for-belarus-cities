from django.urls import path

from users.views import UserLogin, UserRegister

urlpatterns = [
    path('register/', UserRegister.as_view(template_name='register.html'), name='register'),
    # path('profile/', UserProfile.as_view, name='profile'),
    path('login/', UserLogin.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('please_login/', auth_views.LoginView.as_view(template_name='please_login.html'), name='please_login'),
]
