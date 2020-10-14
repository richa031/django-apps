from django.shortcuts import render

#take all the requests and sends back an http response
from django.http import Http404 
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album


def index(request):
    all_albums = Album.objects.all(); #connecting to db to access all the objects stored
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context) #shortcut to render template

def detail(request, id):
    try:
        album = Album.objects.get(pk=id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})


