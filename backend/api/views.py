from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import (SingerSerializer, SongSerializer,
                             AlbumSerializer, AlbumSongSerializer)
from catalog.models import Singer, Song, Album, AlbumSong


class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumSongViewSet(viewsets.ModelViewSet):
    queryset = AlbumSong.objects.all()
    serializer_class = AlbumSongSerializer
