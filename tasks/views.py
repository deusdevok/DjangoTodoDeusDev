from django.http import HttpResponse
from django.shortcuts import render
from .models import TodoList, TodoItem

def index(request):
    list_objects = TodoList.objects.all()
    context = {
        "list_objects": list_objects,
    }

    return render(request, "tasks/index.html", context)

def todolist(request, todolist_id):
    list_name = TodoList.objects.get(pk=todolist_id)
    todo_items = TodoItem.objects.filter(related_list__id=todolist_id)
    context = {
        "list_name": list_name,
        "list_id": todolist_id,
        "todo_items": todo_items,
    }
    return render(request, "tasks/items.html", context)

def add_items(request, todolist_id):
    new_item_name = request.POST['new_item']
    list_name = TodoList.objects.get(pk=todolist_id)
    
    new_item_object = TodoItem()
    new_item_object.item_name = new_item_name
    new_item_object.related_list = list_name
    new_item_object.save()

    todo_items = TodoItem.objects.filter(related_list__id=todolist_id)
    context = {
        "list_name": list_name,
        "list_id": todolist_id,
        "todo_items": todo_items,
    }
    return render(request, "tasks/items.html", context)

def listitems(request, todolist_id):
    response = "This are the items from the todo list {}".format(todolist_id)
    return HttpResponse(response)