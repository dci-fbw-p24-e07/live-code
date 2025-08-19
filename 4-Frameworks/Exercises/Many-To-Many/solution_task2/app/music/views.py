"""Solutions to task 2."""
from django.contrib.auth.models import User
from django.db.models import F, Q

from music.models import Author, Musician, Profile, Song


class Task2:

    def subtask1(self):
        """Assign the song with id 15 to the authors with ids 30 and 40."""
        # They can be created in one instruction
        return Song.objects.get(pk=15).authors.add(
            Author.objects.get(pk=30), Author.objects.get(pk=40)
        )

    def subtask2(self):
        """Assign the songs with ids 10, 20, 30 1nd 40 to the author with id 50."""
        return Author.objects.get(pk=50).song_set.add(
            Song.objects.get(pk=10), Song.objects.get(pk=20),
            Song.objects.get(pk=30), Song.objects.get(pk=40)
        )

    def subtask3(self):
        """Assign the musicians with ids 10, 20, 30 and 40 to the author with id 100."""
        return Author.objects.get(pk=100).members.set(
            [
                Musician.objects.get(pk=10),
                Musician.objects.get(pk=20),
                Musician.objects.get(pk=30),
                Musician.objects.get(pk=40)
            ],
            through_defaults={"start": 1997, "end": 1998}
        )

    def subtask4(self):
        """Get the name and instrument of each member (musician) of the band (author) with id 100."""
        return Author.objects.get(pk=100).members.all().values("name", "instrument")
