from django.shortcuts import render

#take all the requests and sends back an http response
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is our app homepage</h1>")

