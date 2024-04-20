from django import forms
from .models import Task

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput)




class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','desc','deadline']

        
class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','desc','deadline', 'status']
