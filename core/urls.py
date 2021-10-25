from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('task', newTask, name="new.task"),
    path('task/check/<int:id>', checkTaks, name="task.check"),
    path('task/uncheck/<int:id>', uncheckTaks, name="task.uncheck")
]