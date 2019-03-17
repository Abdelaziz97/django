from django.shortcuts import render
from .models import Client, Project, Task

def home(request):
    context = {
        'projects': Project.objects.all(),
        'title': "Bogoss"
    }
    return render(request, 'blog/home.html', context)

def client(request):
    return render(request, 'blog/client.html')

def user(request):
    return render(request, 'blog/user.html')
