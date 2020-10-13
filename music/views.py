from django.shortcuts import render

#take all the requests and sends back an http response
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is our app homepage</h1>")

def detail(request, id):
    return HttpResponse("<h2>Details for Album id: " + str(id) + "</h2>")


