from django.shortcuts import render
from .models import Item


def get_todo_list(request):
    # Query the database for all items of the Item model
    items = Item.objects.all()  # returns a QuerySet
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
