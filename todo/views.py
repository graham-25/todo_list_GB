from django.shortcuts import render, redirect
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
    if request.method == 'POST':  # This starts a post request
        form = ItemForm(request.POST)
        name = request.POST.get('item_name') # We get the information from the form that comes in with this template. 
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list') # Back to the get_todo_list url name 
    form = ItemForm() # We creating an instance of the form
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context) # this one is if it's a get request.
