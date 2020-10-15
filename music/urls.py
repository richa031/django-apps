from django.urls import path
from . import views #look for views.py in the same directory

app_name = 'music' #namespacing urls 

urlpatterns = [
    #/music/
    path('', views.IndexView.as_view(), name='index'), #index is the home page of the section in views.py
    #/music/<album_id>/
    path('<pk>/', views.DetailView.as_view(), name='detail'), #name is used to remove hardcoded urls
]