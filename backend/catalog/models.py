from django.db import models


class Singer(models.Model):
    """Модель исполнителей."""

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
        ordering = ('name', )

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text='Название команды',
        verbose_name='Название',
    )

    def __str__(self):
        return f'{self.name}'
