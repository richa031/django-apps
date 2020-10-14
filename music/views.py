from django.shortcuts import render

#take all the requests and sends back an http response
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #seperating html from main code
from .models import Album


def index(request):
    all_albums = Album.objects.all(); #connecting to db to access all the objects stored
    template = loader.get_template('music/index.html') #django in default view will look into this file no need to write complete address
    context = {#we pass the album info using this dict to our template
        'all_albums': all_albums, 
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    return HttpResponse("<h2>Details for Album id: " + str(id) + "</h2>")


