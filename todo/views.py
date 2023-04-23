from django.shortcuts import get_object_or_404, render, redirect
from .models import Item
from .forms import AddItemForm, EditItemForm


def get_todo_list(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.done = False
            item.save()
            return redirect('get_todo_list')
    else:
        form = AddItemForm()
        # Query the database for all items of the Item model
        # returns json converted from a QuerySet
        items = Item.objects.all().values()
        context = {
            'items': items,
            'form': form
        }
        return render(request, 'todo/index.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')


def edit_item(request, item_id):
    instance = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = EditItemForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    else:
        form = EditItemForm(instance=instance)

    items = Item.objects.all().values()
    context = {
        'items': items,
        'form': form,
        'edit_item_id': item_id,
    }
    return render(request, 'todo/index.html', context)
