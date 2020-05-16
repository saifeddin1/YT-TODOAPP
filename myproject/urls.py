from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]
























    # path('delete_completed/', delete_completed, name="delete_completed"),