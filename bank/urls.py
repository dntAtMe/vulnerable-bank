from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='bank/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bank/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]