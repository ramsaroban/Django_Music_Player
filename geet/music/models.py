from django.db import models
from django.core.urlresolvers import reverse

class Album_geet(models.Model):

    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
       return reverse('music:album_details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title

class Song_geet(models.Model):

    album = models.ForeignKey(Album_geet, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

    def get_absolute_url(self):
        return reverse('music:album_details', kwargs={'pk': self.album.pk})