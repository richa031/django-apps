from django.urls import path
from . import views #look for views.py in the same directory

app_name = 'music' #namespacing urls 

urlpatterns = [
    #/music/
    path('', views.index, name='index'), #index is the home page of the section in views.py
    #/music/<album_id>/
    path('<int:id>/', views.detail, name='detail'), #name is used to remove hardcoded urls
    #music/<album_id>/favorite/
    path('<int:id>/favorite/', views.favorite, name='favorite'), #some urls return a functionality like login 
]