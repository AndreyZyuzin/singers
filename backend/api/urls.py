from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (AlbumsViewSet, AlbumSongViewSet,
                       SingerViewSet, SongViewSet,)

v1_router = DefaultRouter()
v1_router.register('singers', SingerViewSet, basename='singer')
v1_router.register('songs', SongViewSet, basename='song')
v1_router.register('albums', AlbumsViewSet, basename='album')
v1_router.register('songs2', AlbumSongViewSet, basename='song2')



urlpatterns = [
    path('', include(v1_router.urls))
]
