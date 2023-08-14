from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user', views.user, name='user'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('user_page', views.user_page, name='user_page'),
    path('logout', views.logout, name='logout'),
]