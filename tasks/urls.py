from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),                            # /tasks/
    path("<int:todolist_id>/", views.todolist, name="todolist"),    # /tasks/23/
    path("<int:todolist_id>/items/", views.listitems, name="listitems") # /tasks/23/items/
]