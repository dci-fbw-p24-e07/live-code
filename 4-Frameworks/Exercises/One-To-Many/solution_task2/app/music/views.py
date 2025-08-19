"""Solutions to task 2."""
from datetime import datetime

from music.models import Album, Author, Musician, Song


class Task2:

    def subtask1(self):
        """Show a list of all musicians playing in the song with id `46`."""
        return Musician.objects.filter(author__song__pk=46)

    def subtask2(self):
        """Get the producer of the song with id `13`."""
        return Song.objects.select_related("album").get(pk=13).album.produced_by
        # Alternatively ...
        song = Song.objects.filter(pk=13).values("album__produced_by")[0]
        return song["album__produced_by"]

    def subtask3(self):
        """Show the id, title and album title of all `pop` songs having a Saxophone."""
        return Song.objects.filter(
            style="Pop", author__members__instrument="sax"
        ).values("pk", "title", "album__title").distinct("pk")
        # To count them ...
        return Song.objects.filter(
            style="Pop", author__members__instrument="sax"
        ).values("pk", "title", "album__title").distinct("pk").count()

    def subtask4(self):
        """Show the id, title and album title of all songs produced by `Clark` and having a Saxophone."""
        return Song.objects.filter(
            album__produced_by="Clark", author__members__instrument="sax"
        ).values("id", "title", "album__title").distinct("pk")
        # To count them ...
        return Song.objects.filter(
            album__produced_by="Clark", author__members__instrument="sax"
        ).values("id", "title", "album__title").distinct("pk").count()

    def subtask5(self):
        """Show all producers of bands that first appeared in the last hundred years."""
        return Album.objects.filter(
            song__author__first_appearance__gte=datetime.today().year - 100
        ).values("produced_by").distinct("produced_by")
        # To count them ...
        return Album.objects.filter(
            song__author__first_appearance__gte=datetime.today().year - 100
        ).values("produced_by").distinct("produced_by").count()
