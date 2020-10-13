from django.contrib import admin
from .models import Album
from .models import Song

#show my tables in django admin page
admin.site.register(Album) 
admin.site.register(Song)
