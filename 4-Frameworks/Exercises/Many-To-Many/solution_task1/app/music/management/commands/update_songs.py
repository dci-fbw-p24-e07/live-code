"""Creates and loads fake data."""
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from music.models import Song
from django.contrib.auth.models import User
import random
import json

BASE_DIR = Path(__file__).resolve().parent


class Command(BaseCommand):
    """Update created_by and last_modified_by in the songs table."""

    help = 'Update the fields created_by and last_modified_by'

    def handle(self, *args, **options):
        users = {}
        for user in User.objects.all():
            users.update({user.username: user})
        with open("music/management/commands/song_created_updated_map.json") as data:
            map = json.loads(data.read())
            objects = []
            for song_id, creator, updater in map:
                song = Song.objects.get(pk=song_id)
                song.created_by = users[creator]
                song.last_modified_by = users[updater]
                objects.append(song)
            Song.objects.bulk_update(objects, ["created_by", "last_modified_by"])

    def create_random_data(self):
        users = User.objects.all()
        num_users = len(users)
        map = []
        for song in Song.objects.all():
            creator = random.randint(0, num_users - 1)
            updater = random.randint(0, num_users - 1)
            map.append([song.pk, users[creator].username, users[updater].username])
        print(json.dumps(map))
