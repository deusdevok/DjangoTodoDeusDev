from django.contrib import admin
from .models import TodoList, TodoItem

admin.site.register(TodoList)

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'related_list']

admin.site.register(TodoItem, TodoItemAdmin)
