from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework import status

from catalog.models import Singer, Song, Album, AlbumSong


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Singer


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Song


class AlbumSongSerializer(serializers.ModelSerializer):
    # album = serializers.ReadOnlyField(source='album.name')
    name = serializers.ReadOnlyField(source='song.name')

    class Meta:
        fields = '__all__'
        fields = ('name', 'number',)
        model = AlbumSong


class AlbumSerializer(serializers.ModelSerializer):
    singer = serializers.ReadOnlyField(source='singer.name')
    songs = AlbumSongSerializer(many=True, source='albums')

    class Meta:
        fields = ('id', 'name', 'singer', 'year', 'songs')
        model = Album

    def create(self, validated_data):
        singer_id = self.initial_data.pop('singer')
        try:
            singer = Singer.objects.get(pk=singer_id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                detail=f'Не найден исполнитель с id={singer_id}.',
                code=status.HTTP_400_BAD_REQUEST,
            )

        songs = self.initial_data.pop('songs')
        try:
            for item in songs:
                item_id = item['song']
                Song.objects.get(pk=item_id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                detail=f'Не существует песня c id={item_id}.',
                code=status.HTTP_400_BAD_REQUEST,
            )

        album = Album.objects.create(
            name=self.initial_data['name'],
            singer=singer,
            year=self.initial_data['year'],
        )
        album.save()
        for item in songs:
            song = AlbumSong.objects.create(
                album=album,
                song=Song.objects.get(pk=item['song']),
                number=item['number']
            )
        return album
