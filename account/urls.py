from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    # post views
    # path('login/', views.user_login, name='login'),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LoginView.as_view(), name='logout')
]