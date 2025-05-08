from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.http import request, HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.

@login_required
def dashboard(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request,'task/dashboard.html',{'tasks':tasks})

@login_required
def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    people_list = User.objects.all()
    return render(request, 'task/create.html', {'form': form,'people_list':people_list})

@login_required
def edit_task(request):
    if request.method == 'POST':
        id = request.GET.get('id')
        task_obj = Task.objects.get(id=id)
        form = TaskForm(request.POST, instance=task_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    id = request.GET.get('id')
    task_obj = Task.objects.get(id=id)
    form = TaskForm(instance=task_obj)
    return render(request,'task/edit.html',{'tasks':task_obj,'form': form})

@login_required
def delete_task(request):
    if request.method=="POST":
        id = request.POST.get('id')
        task_obj = Task.objects.get(id=id)
        task_obj.delete()
        return HttpResponseRedirect('/')