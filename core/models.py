from django.db import models
from django.forms import ModelForm

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'done'
        ]