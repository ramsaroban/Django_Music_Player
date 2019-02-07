from django.views import generic

from music.forms import UserForms
from .models import Album_geet
from .models import Song_geet
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic  import View

class IndexView(generic.ListView):
    #template name
    template_name = 'music/index.html'
    context_object_name = "all_album"

    def get_queryset(self):
        #import pdb;pdb.set_trace()#def function to get all album lisi
        return Album_geet.objects.all()

class SongView(generic.ListView):
    template_name = 'music/song_details.html'
    context_object_name = 'all_songs'

    def get_queryset(self):
        return Song_geet.objects.all()

class DetailView(generic.DetailView):
    model = Album_geet
    template_name = 'music/album_details.html'
    context_object_name = 'album_details'

    #def get_queryset(self):
     #  return Song_geet.objects.all()


class Album_geetCreate(CreateView):
    model = Album_geet
    fields = ['artist', 'album_title', 'genre', 'album_logo', 'is_favorite']


class Album_geeUpdate(UpdateView):
    model = Album_geet
    fields = ['artist', 'album_title', 'genre', 'album_logo', 'is_favorite']

class Album_geetDelete(DeleteView):
    model = Album_geet
    success_url = reverse_lazy('music:index')

class  Album_geetFavoite(UpdateView):
    model = Album_geet
    fields = ['is_favorite']
    success_url = reverse_lazy('music:index')

class Song_geetCreate(CreateView):
    model = Song_geet
    fields = ['album','song_title', 'audio_file', 'is_favorite']


#User registration and login
class UserFormsView(View):
    form_class = UserForms
    #template_name = 'music/user_registraion.html'