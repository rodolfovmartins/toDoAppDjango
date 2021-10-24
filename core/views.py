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
    next = request.POST.get('next', '/')
    try:
        if request.POST:
            taskModelForm = TaskForm(request.POST)
            if taskModelForm.is_valid():
                task = taskModelForm.save()
                messages.success(request, 'New task registered')
            else:
                messages.error(request, taskModelForm.errors)

        return HttpResponseRedirect(next)
    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(next)


