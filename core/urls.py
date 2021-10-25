from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('task', newTask, name="new.task"),
    path('task/update', updateTask, name="task.update"),
    path('task/delete/<int:id>', deleteTask, name="task.delete"),
    path('task/check/<int:id>', checkTask, name="task.check"),
    path('task/uncheck/<int:id>', uncheckTask, name="task.uncheck")
]