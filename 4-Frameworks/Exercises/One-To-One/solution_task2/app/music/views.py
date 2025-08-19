"""Solutions to task 2."""
from django.contrib.auth.models import User
from django.db.models import F, Q

from music.models import Profile, Song


class Task2:

    def subtask1(self):
        """Create 5 users **with profiles**."""
        # They can be created in one instruction
        Profile.objects.create(
            user=User.objects.create_user("josephine", "jo@example.com", "one"),
            preferred_style="Pop",
            preferred_song_id=13
            )
        Profile.objects.create(
            user=User.objects.create_user("grumilda", "gru@example.com", "two"),
            preferred_style="Funky",
            preferred_song_id=45
            )
        Profile.objects.create(
            user=User.objects.create_user("stanis", "stan@example.com", "three"),
            preferred_style="Rock",
            preferred_song_id=44
            )
        Profile.objects.create(
            user=User.objects.create_user("lucifer", "lu@example.com", "four"),
            preferred_style="Indie",
            preferred_song_id=2
            )
        # And they can be created with two instructions
        admin = User.objects.create_superuser("superadmin", "admin@example.com", "admin")
        Profile.objects.create(user=admin, preferred_style="Funky",
                               preferred_song_id=3)
        # Return the username and preferred style and song of all users
        return User.objects.values(
            "username", "profile__preferred_style", "profile__preferred_song"
        )

    def subtask2(self):
        """Update created_by and last_modified_by."""
        admin = User.objects.get(username="superadmin")
        return Song.objects.all().update(created_by=admin, last_modified_by=admin)

    def subtask3(self):
        """Return all songs having Josephine's preferred style."""
        return Song.objects.filter(
            style=Profile.objects.get(user__username="josephine").preferred_style
        )

    def subtask4(self):
        """Show the preferred styles of the users who created songs with a Tambourine."""
        return Song.objects.filter(
            author__members__instrument="tambourine"
        ).distinct("created_by__profile__preferred_style").values("created_by__profile__preferred_style")

    def subtask5(self):
        """Show the preferred songs of all users who created piano songs from the eighties or ukulele songs from 1910-1919."""
        piano_eighties = Q(author__members__instrument="piano",
                           author__first_appearance__gte=1980,
                           author__first_appearance__lte=1989)
        ukulele_tens = Q(author__members__instrument="ukulele",
                         author__last_appearance__gte=1910,
                         author__last_appearance__lte=1919)
        return (Song.objects.filter(piano_eighties | ukulele_tens)
                .annotate(song_id=F("created_by__profile__preferred_song"),
                          song_title=F("created_by__profile__preferred_song__title"))
                .distinct("song_id").values("song_id", "song_title"))
        # Or
        return (Song.objects.filter(piano_eighties | ukulele_tens)
                .distinct("created_by__profile__preferred_song")
                .values("created_by__profile__preferred_song",
                        "created_by__profile__preferred_song__title"))
