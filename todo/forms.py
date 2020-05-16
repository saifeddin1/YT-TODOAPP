from django import forms
from .models import Task 
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User 


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task 
		fields = ('name',)


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User 
		fields = ('username', 'email','password1','password2',)
		widgets = {
			'username': forms.TextInput(attrs={
						'class':'form-control',
						'placeholder':'Username',
				}),
			'email': forms.EmailInput(attrs={
						'class':'form-control',
						'placeholder':'email',
				}), 
		}