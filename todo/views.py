from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, CreateUserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth.decorators import login_required



@login_required
def index(request):

	tasks = Task.objects.all()
	form = TaskForm() 
	if request.method == 'POST':
		form = TaskForm(request.POST) 
		if form.is_valid():
			form.save()
			return redirect('index')

	context = {'all_tasks':tasks, 
				'task_form':form, #template var
				}

	return render(request, 'todo/index.html', context)


def complete_task(request, task_id):
	task = Task.objects.get(id=task_id)
	task.completed = True 
	task.save()
	return redirect('index')


def delete_completed(request):
	completed_tasks = Task.objects.filter(completed=True)
	completed_tasks.delete()
	return redirect('index')


def delete_all(request):
	tasks = Task.objects.all()
	tasks.delete()
	return redirect('index')


def register(request):
	if request.user.is_authenticated:
		return redirect('index')
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')

	context = {'registration_form':form} 
	return render(request, 'todo/register.html', context)


def login(request):
	if request.user.is_authenticated:
		return redirect('index')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
	
		if user is not None:
			auth_login(request, user) 
			return redirect('index')
		
	return render(request, 'todo/login.html')


def logout(request):
	auth_logout(request)
	return redirect('login')














# def delete_all(request):
# 	# bring all tasks
# 	tasks = Task.objects.all()
# 	#delete theese
# 	tasks.delete()
# 	#redirect index


# def delete_completed(request):
# 	#bring the completed tasks
# 	tasks = Task.objects.filter(completed=True)
# 	#delete
# 	tasks.delete()

# 	#redirect index 
# 	return redirect('index')
