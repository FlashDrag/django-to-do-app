from django.shortcuts import render, redirect
from .models import Item


def get_todo_list(request):
    # Query the database for all items of the Item model
    items = Item.objects.all()  # returns a QuerySet
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == "POST":
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')
