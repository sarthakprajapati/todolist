from django.forms import ModelForm
from .models import todolist
from django import forms

class todoform(forms.ModelForm):
    class Meta:
        model = todolist
        fields = ['title', 'description', 'date', 'active']












