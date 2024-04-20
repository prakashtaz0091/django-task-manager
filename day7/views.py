from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required,  permission_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# from django.views.decorators.http import require_POST

from . import forms

from . import models
# Create your views here.
@login_required
def index(request):

    tasks = models.Task.objects.filter(user=request.user)


    if request.method=="POST":
        add_task_form_data = forms.AddTaskForm(data=request.POST)
        # print(add_task_form_data)
        if add_task_form_data.is_valid():
            print(type(add_task_form_data.cleaned_data))
            
            # add_task_form_data.cleaned_data['user'] = request.user
            # add_task_form_data.save()
            # print(add_task_form_data.cleaned_data)
            cleaned_data = add_task_form_data.cleaned_data

            task_title = cleaned_data.get('title')
            task_desc = cleaned_data.get('desc')
            task_deadline = cleaned_data.get('deadline')
            task_user = request.user

            models.Task.objects.create(
                user = task_user,
                title = task_title,
                desc = task_desc,
                deadline = task_deadline
            )

        

            return redirect("day7:index")

        else:
            return HttpResponse("Invalid Form Data")


    else:
        context = {
            'user':request.user,
            'add_task_form':forms.AddTaskForm,
            'tasks':tasks[::-1],


        }
        return render(request, 'day7/index.html', context)


  


def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('day7:index')
    else:
        form = forms.LoginForm()
    return render(request, 'day7/login.html', {'login_form': form})


def logout_view(request):
    logout(request)
    return redirect('day7:login_view')


def update_task(request, task_id):

    if request.method=="POST":
        add_task_form_data = forms.UpdateTaskForm(data=request.POST)
        if add_task_form_data.is_valid():
            cleaned_data = add_task_form_data.cleaned_data
            task = models.Task.objects.get(id=task_id)
            task.title = cleaned_data.get('title')
            task.desc = cleaned_data.get('desc')
            task.deadline = cleaned_data.get('deadline')
            task.status = cleaned_data.get('status')
            task.save()
            return redirect('day7:index')
        else:
            return HttpResponse("Invalid Form Data")
    else:
        task = models.Task.objects.get(id=task_id)

        context = {
        
            'add_task_form':forms.UpdateTaskForm(instance=task),

        }
        return render(request, 'day7/update.html', context)




def delete_task(request, task_id):
    task = models.Task.objects.get(id=task_id)
    task.delete()
    return redirect('day7:index')



def order_by_date(request):
    tasks = models.Task.objects.filter(user=request.user).order_by('deadline')

    context = {
        'tasks':tasks,
        'user':request.user,
        'add_task_form':forms.AddTaskForm,
    }
    return render(request,'day7/index.html', context)



def search(request):
    search_text = request.GET.get('search_text')
    tasks = models.Task.objects.filter(title__icontains=search_text)
    context = {
        'tasks':tasks,
        'user':request.user,
        'add_task_form':forms.AddTaskForm,
    }
    return render(request,'day7/index.html', context)