from django.shortcuts import render, HttpResponseRedirect
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)

def newTask(request):
    if request.POST:
        name = request.POST.get('name')
        Task.objects.create(name=name)

    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)