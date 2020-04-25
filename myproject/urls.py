from django.contrib import admin
from django.urls import path
from todo.views import index, complete_task, delete_completed, delete_all

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('complete/<int:task_id>/', complete_task, name="complete"),
    path('delete_completed/', delete_completed, name="delete_completed"),
    path('delete_all/', delete_all, name="delete_all"),




]
























    # path('delete_completed/', delete_completed, name="delete_completed"),