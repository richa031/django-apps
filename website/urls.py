#first page which server looks for
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')), #this is gonna include our apps urls to main urls
    path('music/', include('music.urls')),
]
