from django.urls import path
from .views import ProjectListView
from . import views

urlpatterns = [
    path('', ProjectListView.as_view(), name='blog-home'),
    path('client', views.client, name='blog-client'),
    path('user', views.user, name='blog-user'),
]