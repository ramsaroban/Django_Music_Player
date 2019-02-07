from django.conf.urls import url

from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    #music/<id>
    #url(r'^(?P<album_title>\w*\s*\w*)$', views.album_details, name='album_details'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='album_details'),
    url(r'^album/add/$', views.Album_geetCreate.as_view(), name='add-album'),

    url(r'^song/add/$', views.Song_geetCreate.as_view(), name='add-songs'),

    url(r'^songs/$', views.SongView.as_view(), name='all-songs'),

    #/musicalbumUpdate/2
    url(r'^albumUpdate/(?P<pk>[0-9]+)/$', views.Album_geeUpdate.as_view(), name='album-update'),
    #/music/albumDelete/2
    url(r'^albumDelete/(?P<pk>[0-9]+)/$', views.Album_geetDelete.as_view(), name='album-delete'),

#/music/albumDelete/2
    url(r'^albumFavorite/(?P<pk>[0-9]+)/$', views.Album_geetFavoite.as_view(), name='album-favorite'),
]

