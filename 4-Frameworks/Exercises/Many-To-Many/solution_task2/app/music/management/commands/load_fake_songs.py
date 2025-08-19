"""Creates and loads fake data."""
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from music.models import Album, Author, Musician, Song
from django.core.files import File
import random
from datetime import datetime, timedelta

BASE_DIR = Path(__file__).resolve().parent

FIRST_NAMES = ('Abdul', 'David', 'Julia', 'Arnold', 'Bernhard', 'Gerald', 'Anna', 'Yussef', 'Itziar', 'Olivia', 'Emma', 'Amelia', 'Mia', 'Chloe', 'Penelope', 'Grace', 'Layla', 'Ella', 'Abigail', 'Camila', 'Gianna', 'Evelyn', 'Aaliyah', 'Naomi', 'Aarya', 'Araceli', 'Yamileth', 'Loretta', 'Liam', 'Noah', 'William', 'Lucas', 'Benjamin', 'Marc', 'Oriol', 'Arturo', 'Keith', 'Zain', 'Johann', 'Nikolas', 'Ahmed')

LAST_NAMES = ('Smith', 'Blanc', 'Müller', 'Miller', 'Muller', 'Griesebner', 'Hutticher', 'Karnasiotti', 'Martí', 'Vidal', 'Masferrer', 'Doe', 'Adams', 'Anniston', 'Hunter', 'Schwarzenegger', 'White', 'Black', 'Green', 'Schumacher', 'Perez', 'Fiedler', "O''Connor", "McDonald", 'Johnson', 'Williams', 'Brown', 'Garcia', 'Jones', 'Davis', 'Wilson', 'Moore', 'Jackson', 'Lee', 'Ali', 'Ahmas', 'Sanchez', 'Clark', 'Hill', 'Young', 'Wright', 'Lewis', 'Nguyen', 'Allen')

BANDS = ("The Troublemakers", "The back-enders", "Guido & The Django Band", "Ant", "Butterlies", "The Jumping Stones", "The Back-end Boys", "Djangstein")

NATIONALITIES = ("DE", "FR", "EN", "IT", "SP", "US", "GR", "PT", "RU", "IN")


class Command(BaseCommand):
    """Create and load fake data."""

    help = 'Create and load fake data'
    albums = 100
    author = 80
    max_songs_per_album = 15
    max_members_in_author = 8

    def handle(self, *args, **options):
        Song.objects.all().delete()
        objects = []
        for album_id in range(1, self.albums + 1):
            album = Album(**self.get_random_album(album_id))
            album.save()
            author = Author(**self.get_random_author(album_id))
            author.save()
            if random.random() > 0.7:
                musician = Musician.objects.create(author=author, **self.get_random_musician(name=author.name))
            else:
                for musician_id in range(1, random.randint(2, self.max_members_in_author + 1)):
                    Musician.objects.create(author=author, **self.get_random_musician())

            for song_id in range(1, random.randint(2, self.max_songs_per_album + 1)):
                song = Song(album=album, author=author, **self.get_random_song(song_id))
                song.save()
                print(album.pk, song.pk)

            # objects.append(Song(**self.get_random_data(counter)))
        # Song.objects.bulk_create(objects)
        print(Song.objects.count(), "songs have been loaded.")

    def get_random_musician(self, name=None):
        if name is None:
            name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        instrument = random.choice([choice[0] for choice in Musician._meta.get_field("instrument").choices])
        return {
            "name": name,
            "nationality": random.choice(NATIONALITIES),
            "instrument": instrument
        }

    def get_random_album(self, counter):
        """Return a random dictionary."""
        return {
            "title": f"Album {counter}",
            "year_of_release": random.randint(1000, datetime.today().year),
            "produced_by": f"{random.choice(LAST_NAMES)}"
        }

    def get_random_author(self, counter):
        """Return a random dictionary."""
        name = random.choice(BANDS)
        if random.random() > 0.3:
            name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        first_appearance = random.randint(1000, datetime.today().year)
        return {
            "name": name,
            "website": "https://www.google.com",
            "first_appearance": first_appearance,
            "last_appearance": random.randint(first_appearance, datetime.today().year)
        }

    def get_random_song(self, counter):
        """Return a random dictionary of data."""
        audio = open(BASE_DIR / "sample.mp3", "rb")
        max_duration = 360
        max_price = 4.99
        style = random.choice([choice[0] for choice in Song._meta.get_field("style").choices])
        price = "{:0.2f}".format(random.random() * max_price)
        return {
            "audio": File(audio, name="sample.mp3"),
            "style": style,
            "title": f"Audio number {counter + 1}",
            "duration": timedelta(seconds=random.randint(0, max_duration)),
            "price": price,
            "deal_of_the_day": random.random() > 0.9,
            "playbacks": random.randint(0, 2000)
        }
