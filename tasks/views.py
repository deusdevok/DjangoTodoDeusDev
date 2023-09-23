from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! This is the tasks view.")

def todolist(request, todolist_id):
    response = "This is the todo list {}".format(todolist_id)
    return HttpResponse(response)

def listitems(request, item_id):
    response = "This are the items from the todo list {}".format(item_id)
    return HttpResponse(response)