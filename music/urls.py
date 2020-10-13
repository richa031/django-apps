from django.urls import path
from . import views #look for views.py in the same directory

urlpatterns = [
    #/music/
    path('', views.index, name='index'), #index is the home page of the section in views.py
    path('<int:id>/', views.detail, name='detail'),
]