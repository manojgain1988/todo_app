from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.


def index(request):
    if request.method == 'POST':
        text = request.POST.get("text").strip()
        if text:
            Todo.objects.create(text=text)
        return redirect('/')

    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)


def deleteTodo(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('/')



def about(request):
    return render(request, 'about.html')



def login(request):
    return render(request, 'login.html')



def register(request):
    return render(request, 'register.html')

