from django.contrib import admin
from django.contrib.auth.models import Group, User

from catalog.models import Album, AlbumSong, Singer, Song


class AlbumSongInline(admin.TabularInline):
    model = AlbumSong
    extra = 0


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'singer', 'year')
    list_display_links = ('name', 'singer',)
    list_editable = ('year',)
    inlines = (AlbumSongInline,)


admin.site.register(Album, AlbumAdmin)
admin.site.register(Singer)
admin.site.register(Song)

admin.site.unregister(User)
admin.site.unregister(Group)
