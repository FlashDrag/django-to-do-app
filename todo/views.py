from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


def get_todo_list(request):
    # Query the database for all items of the Item model
    items = Item.objects.all()  # returns a QuerySet
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)
