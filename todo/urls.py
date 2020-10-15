from django.urls import path
from . import views #look for views.py in the same directory

app_name = 'todo' #namespacing urls 

urlpatterns = [
    #/todo/
    path('', views.index, name='index'), #index is the home page of the section in views.py
]