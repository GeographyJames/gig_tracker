from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('register/', views.register, name='register')

]