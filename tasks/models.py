from django.db import models

class TodoList(models.Model):
    list_name = models.CharField(max_length=250)

    def __str__(self):
        return self.list_name

class TodoItem(models.Model):
    item_name = models.CharField(max_length=250)
    related_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    mark_done = models.BooleanField(default=False) # New

    def __str__(self):
        return self.item_name
