from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import Create_Task
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'data_todolist': data_todolist,
        'username': request.user,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        form = Create_Task(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.date_task = (datetime.date.today())
            new_task.save()
            messages.success(request, 'Task berhasil ditambahkan!')
            return redirect('todolist:show_todolist')
    else:
        form = Create_Task()
    
    return render(request, 'task.html', {'form' : form})

def show_todolist_json(request):
    task_data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", task_data), content_type="application/json")

@csrf_exempt
def add_todolist (request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        new_task = Task.objects.create(
            date_task = (datetime.date.today()),
            title = title,
            description= description,
            user = request.user
        )
        res = {
            'fields':{
                'date_task':new_task.date_task,
                'judul':new_task.title,
                'desc':new_task.description,
            },
            'pk':new_task.pk
        }
        return JsonResponse(res)