# Add all your views here
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from datetime import datetime, timedelta

current_tasks = []
completed_tasks = []


def home_page(request):

    datetime_now = datetime.strftime(datetime.now() + timedelta(hours=5, minutes=30),"%dth %B, %Y %A, %I:%M %P")

    hobbies = ['Singing','Play guitar','Coding',"Running", "Drinking Alcohol", "Smoking", "Dancing"]
    
    context = {
        'name' : "Akshay",
        'age'  : 55,
        'place': "Perumanna",
        'status': "",
        'datetime_val': datetime.now() + timedelta(hours=5, minutes=30),
        'f_datetime_val': datetime_now,
        'habits': hobbies 

    }
    return render(request,'polls_home_page.html',context)

def get_task_manager_form(request):
    return render(request,"task_manager.html",context={'tasks':current_tasks})


def add_task(request):
    new_task =request.GET.get('task')
    if new_task:
        current_tasks.append(new_task)
    # return get_task_manager_form(request)
    return HttpResponseRedirect('/tasks/')

def delete_taskno(request,id):
    print(id)
    if current_tasks:
        val = current_tasks.pop(id-1)
    
    return HttpResponseRedirect('/tasks/')


def mark_completed(request,index):
    if current_tasks:
        val = current_tasks.pop(index-1)
        if val:
            completed_tasks.append(val)
    
    return HttpResponseRedirect('/tasks/')


def render_completed_tasks(request):
    return render(request,'view_completed_tasks.html',context={'tasks_completed':completed_tasks})


def render_all_tasks(request):
    return render(request,'render_all_tasks.html',context = {'pending_tasks':current_tasks, 'completed_tasks':completed_tasks})