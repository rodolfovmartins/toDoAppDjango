from django.urls import path
from .views import index, newTask

urlpatterns = [
    path('', index),
    path('task', newTask, name="new.task")
]