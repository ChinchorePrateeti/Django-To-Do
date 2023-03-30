from django.shortcuts import render, redirect
from django.http import HttpResponse

#importing all the data from model
from . models import *
from .forms import *


# Create your views here.
# in django, a views.py is a request handler.
# in django, what users see is templete and not view.

def index(request):
    #grabbing tasks' information from model or database
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        # / is the home page    
        return redirect("/")


    #passing the data and holding it in dictionary named context
    context = {'tasks': tasks, 'form': form}
    return render(request, 'hello.html', context)

def updateTask(request, primaryKey):

    #Task is the name of our model
    #grabbing item and id
    tasks = Task.objects.get(id=primaryKey)

    form = TaskForm(instance=tasks)
    if request.method == 'POST':
        # if instance param is not passed, it will create a new instance as in the above
        form = TaskForm(request.POST, instance=tasks)

        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}

    return render(request, 'updateTask.html', context)


def deleteTask(request, primaryKey):
    this_item = Task.objects.get(id=primaryKey)

    if request.method == 'POST':
        this_item.delete()
        #.save() is not done cz nothing is getting saved to the db, rather deleted.
        # now redirect to the list i.e hello.html, i.e '/'
        return redirect('/')
    context = {'this_item': this_item}
    return render(request, 'deleteTask.html', context)