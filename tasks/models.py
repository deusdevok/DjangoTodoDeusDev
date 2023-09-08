from django.db import models

class TodoList(models.Model):
    list_name = models.CharField(max_length=250)

class TodoItem(models.Model):
    item_name = models.CharField(max_length=250)
    related_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
