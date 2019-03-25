from django.shortcuts import render
from django.views.generic import ListView
from .models import Client, Project, Task

def home(request):
    context = {
        'projects': Project.objects.all(),
        'title': "Bogoss"
    }
    return render(request, 'blog/home.html', context)

class ProjectListView(ListView):
    model = Project
    template_name = 'blog/home.html' # default : <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['startDate'] # '-startDate' for an descending order

def client(request):
    return render(request, 'blog/client.html')

def user(request):
    return render(request, 'blog/user.html')
