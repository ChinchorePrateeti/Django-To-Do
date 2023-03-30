#this file is just a form representation of a models
from django import forms
from django.forms import ModelForm

from .models import *

#name of the form is Taskform
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'