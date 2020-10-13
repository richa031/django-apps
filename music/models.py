#each variable in the class is converted to a column in the table in db
from django.db import models

class Album(models.Model):
    #variable name is same name as col name in table
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self): #string repr of this object
        return self.album_title + ' - ' + self.artist

class Song(models.Model): #we need our song to be a part of any album
    #we need to link these two classes together
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)




