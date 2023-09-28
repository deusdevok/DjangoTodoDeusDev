from django.http import HttpResponse
from django.shortcuts import render
from .models import TodoList

def index(request):
    list_objects = TodoList.objects.all()
    context = {
        "list_objects": list_objects,
    }

    return render(request, "tasks/index.html", context)

def todolist(request, todolist_id):
    response = "This is the todo list {}".format(todolist_id)
    return HttpResponse(response)

def listitems(request, todolist_id):
    response = "This are the items from the todo list {}".format(todolist_id)
    return HttpResponse(response)