from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm # This imports our form we created 

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == 'POST':                # This starts a post request
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')    # Back to the get_todo_list url name 
    form = ItemForm()                           # We creating an instance of the form
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context) # this one is if it's a get request.


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)