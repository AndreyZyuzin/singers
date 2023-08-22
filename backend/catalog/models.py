import logging
from typing import Collection, Optional

from django.db import models
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

class Singer(models.Model):
    """Модель исполнителей."""

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
        ordering = ('name', )

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text='Название исполнителя',
        verbose_name='Название',
    )

    def __str__(self):
        return f'{self.name}'

class Album(models.Model):
    """Модель альбомов."""

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ('name', )

    name = models.CharField(
        max_length=150,
        unique=True,
        help_text='Название альбома',
        verbose_name='Название',
    )

    singer = models.ForeignKey(
        Singer,
        on_delete=models.CASCADE,
        help_text='Исполнитель',
        verbose_name='Исполнитель',
        related_name='albums',
    )

    year = models.PositiveSmallIntegerField(
        help_text='Год альбома',
        verbose_name='Год',
    )

    song = models.ManyToManyField(
        'Song',
        through='AlbumSong',
        help_text='Песня альбома',
        verbose_name='Песня',
    )

    def __str__(self):
        return f'{self.name}'


class Song(models.Model):
    """Модель песенок."""

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

    name = models.CharField(
        max_length=250,
        unique=True,
        help_text='Название песни',
        verbose_name='Название',
    )

    def __str__(self):
        return f'{self.name}'


class AlbumSong(models.Model):
    """Модель для Many To Many, связывающая Song и Album."""

    class Meta:
        verbose_name = 'Песня альбома'
        verbose_name_plural = 'Песни альбома'
        constraints = [
            models.UniqueConstraint(
                fields=['album', 'song'],
                name='unique_album_song',
            )
        ]

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='albums',
        verbose_name='Альбом',
        help_text='Свойства альбома',
    )

    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name='songs',
        verbose_name='Песня',
        help_text='Свойства песни',
    )

    number = models.PositiveSmallIntegerField(
        help_text='Номер песни в альбоме',
        verbose_name='Номер',
    )

#    def clean(self):
#        values = list(AlbumSong.objects.filter(album_id=self.album_id)
#                      .values_list('number', flat=True))
#        if len(values) != len(set(values)):
#            print(f'Повтор. {self.album_id} {self.song_id} {self.number} {values}')
#            raise ValidationError('Недопустим одинаковый номер песни')
#        print(f'ok {self.album_id} {self.song_id} {self.number} {values}')

    def __str__(self):
        return f'{self.song}({self.album})'
