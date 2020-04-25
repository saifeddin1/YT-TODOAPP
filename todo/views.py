from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


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
