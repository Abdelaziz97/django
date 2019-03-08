from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('client', views.client, name='blog-client'),
    path('user', views.user, name='blog-user'),
]