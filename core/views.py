from django.shortcuts import render, HttpResponseRedirect
from .models import Task, TaskForm
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    paginatedTasks = Paginator(tasks, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginatedTasks.get_page(page_number)

    context = {
        'tasks': page_obj
    }
    return render(request, 'index.html', context)

def newTask(request):
    try:
        if request.POST:
            taskModelForm = TaskForm(request.POST)
            if taskModelForm.is_valid():
                taskModelForm.save()
                messages.success(request, 'New task registered')
            else:
                messages.error(request, taskModelForm.errors)

        return HttpResponseRedirect('/')
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect('/')

def checkTask(request, id):
    try:
        task = Task.objects.filter(id=id)
        print(task)
        task.update(done=True)
        return HttpResponseRedirect('/')
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect('/')

def uncheckTask(request, id):
    try:
        task = Task.objects.filter(id=id)
        task.update(done=False)
        return HttpResponseRedirect('/')
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect('/')

def updateTask(request):
    try:
        if request.POST:
            task = Task.objects.get(id=request.POST.get('id'))
            taskModelForm = TaskForm(request.POST, instance=task)

            if taskModelForm.is_valid():
                taskModelForm.save()
                messages.success(request, 'Task updated')
            else:
                messages.error(request, taskModelForm.errors)

        return HttpResponseRedirect('/')
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect('/')
