from django import forms
from todolist.models import Task

class Create_Task(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')