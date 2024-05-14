from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth import authenticate, login as authLogin, logout as authlogout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def index(request): 
    if request.method == 'POST':
        text = request.POST.get("text").strip()
        if text:
            Todo.objects.create(text=text)
        return redirect('/')

    todos = Todo.objects.filter(user=request.user)
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
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            authLogin(request, user)
            messages.add_message(request, messages.SUCCESS, 'Successfully Your Logged in.')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Your Credential are not Valid.')
            return redirect('login')
        
    return render(request, 'login.html')



def register(request):
    return render(request, 'register.html')

