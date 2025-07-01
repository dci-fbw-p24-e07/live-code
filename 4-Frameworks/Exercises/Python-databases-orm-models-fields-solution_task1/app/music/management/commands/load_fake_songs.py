"""Creates and loads fake data."""
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from music.models import Audio
from django.core.files import File
import random
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent

FIRST_NAMES = ('Abdul', 'David', 'Julia', 'Arnold', 'Bernhard', 'Gerald', 'Anna', 'Yussef', 'Itziar', 'Olivia', 'Emma', 'Amelia', 'Mia', 'Chloe', 'Penelope', 'Grace', 'Layla', 'Ella', 'Abigail', 'Camila', 'Gianna', 'Evelyn', 'Aaliyah', 'Naomi', 'Aarya', 'Araceli', 'Yamileth', 'Loretta', 'Liam', 'Noah', 'William', 'Lucas', 'Benjamin', 'Marc', 'Oriol', 'Arturo', 'Keith', 'Zain', 'Johann', 'Nikolas', 'Ahmed')

LAST_NAMES = ('Smith', 'Blanc', 'Müller', 'Miller', 'Muller', 'Griesebner', 'Hutticher', 'Karnasiotti', 'Martí', 'Vidal', 'Masferrer', 'Doe', 'Adams', 'Anniston', 'Hunter', 'Schwarzenegger', 'White', 'Black', 'Green', 'Schumacher', 'Perez', 'Fiedler', "O''Connor", "McDonald", 'Johnson', 'Williams', 'Brown', 'Garcia', 'Jones', 'Davis', 'Wilson', 'Moore', 'Jackson', 'Lee', 'Ali', 'Ahmas', 'Sanchez', 'Clark', 'Hill', 'Young', 'Wright', 'Lewis', 'Nguyen', 'Allen')


class Command(BaseCommand):
    """Create and load fake data."""

    help = 'Create and load fake data'
    amount = 100

    def handle(self, *args, **options):
        Audio.objects.all().delete()
        objects = []
        for counter in range(0, self.amount):
            objects.append(Audio(**self.get_random_data(counter)))
        Audio.objects.bulk_create(objects)
        print(Audio.objects.count(), "songs have been loaded.")

    def get_random_data(self, counter):
        """Return a random dictionary of data."""
        audio = open(BASE_DIR / "sample.mp3", "rb")
        audio_type = random.choice(["song", "podcast", "effect"])
        max_duration = {
            "song": 360,
            "podcast": 3600,
            "effect": 60
        }
        max_price = {
            "song": 4.99,
            "podcast": 3.99,
            "effect": 94.99
        }
        style = None
        if audio_type == "song":
            style = random.choice([choice[0] for choice in Audio._meta.get_field("song_style").choices])
        price = "{:0.2f}".format(random.random() * max_price[audio_type])
        return {
            "audio": File(audio, name="sample.mp3"),
            "type": audio_type,
            "song_style": style,
            "title": f"Audio number {counter + 1}",
            "duration": timedelta(seconds=random.randint(0, max_duration[audio_type])),
            "price": price,
            "deal_of_the_day": random.random() > 0.9,
            "playbacks": random.randint(0, 2000),
            "author": f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}",
            "album": f"Album {random.randint(1, 5)}",
        }
