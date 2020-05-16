from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('complete/<int:task_id>/', complete_task, name="complete"),
    path('delete_completed/', delete_completed, name="delete_completed"),
    path('delete_all/', delete_all, name="delete_all"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout, name="logout")

]
























    # path('delete_completed/', delete_completed, name="delete_completed"),