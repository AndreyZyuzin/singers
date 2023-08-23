from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import (SingerSerializer, SongSerializer,
                             AlbumSerializer, AlbumSongSerializer)
from catalog.models import Singer, Song, Album, AlbumSong


class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

    @action(detail=True, methods=['get'])
    def albums(self, request, pk=None):
        """Отображение все альбомы исполнителя"""
        singer = get_object_or_404(Singer, pk=pk)
        print(f'singer: {singer}')
        print(f'singer albums: {singer.albums.all()}')
        serializer = self.get_serializer(singer.albums.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumSongViewSet(viewsets.ModelViewSet):
    queryset = AlbumSong.objects.all()
    serializer_class = AlbumSongSerializer
