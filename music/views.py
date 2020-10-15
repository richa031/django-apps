#take all the requests and sends back an http response
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all(); #connecting to db to access all the objects stored
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context) #shortcut to render template

def detail(request, id):
    #album = Album.objects.get(pk=id)
    album = get_object_or_404(Album, pk=id)
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, id):
    album = get_object_or_404(Album, pk=id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song']) #getting id of the selected song, 'song' here is the name of input type used
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True 
        selected_song.save() #saving in db
        return render(request, 'music/detail.html', {'album': album})

        


