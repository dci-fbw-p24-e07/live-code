from datetime import datetime, timedelta
from pathlib import Path

from django import db
from django.apps import apps
from django.core.exceptions import ValidationError
from django.core.files import File
from django.test import TestCase

BASE_DIR = Path(__file__).resolve().parent


class Task1(TestCase):

    def setUp(self):
        """Set up."""
        self.album = self.get_model("Album")
        self.song = self.get_model("Song")
        self.author = self.get_model("Author")
        self.musician = self.get_model("Musician")
        self.album_params = {
            "title": "Album test",
            "year_of_release": 2000
        }
        self.author_params = {
            "name": "Author test"
        }
        self.musician_params = {
            "name": "Musician test",
            "nationality": "DE",
            "instrument": "sax",
            "author": self.author.objects.create(**self.author_params)
        }
        audio = open(BASE_DIR / "sample.mp3", "rb")
        self.song_params = {
            "audio": File(audio, name="sample.mp3"),
            "title": "Song test",
            "duration": timedelta(seconds=27)
        }
        super().setUpClass()

    def get_model(self, model_name=None):
        """Return the model if it exists."""
        if not model_name:
            model_name = self.model_name
        try:
            model = apps.get_model("music", model_name)
        except LookupError:
            model = None
        return model

    def test_model_names(self):
        """Test the exstence of the models."""
        self.assertIsNotNone(self.album)
        self.assertIsNotNone(self.song)
        self.assertIsNotNone(self.author)
        self.assertIsNotNone(self.musician)

    def test_required_fields(self):
        """Test the required fields."""
        # Album
        with self.assertRaises(ValidationError) as e:
            self.album.objects.create()
        fields = [error[0] for error in e.exception]
        self.assertEqual(len(fields), 2)
        self.assertIn("year_of_release", fields)
        self.assertIn("title", fields)
        # Song
        with self.assertRaises(ValidationError) as e:
            self.song.objects.create()
        fields = [error[0] for error in e.exception]
        self.assertEqual(len(fields), 3)
        self.assertIn("title", fields)
        self.assertIn("duration", fields)
        self.assertIn("audio", fields)
        # Author
        with self.assertRaises(ValidationError) as e:
            self.author.objects.create()
        fields = [error[0] for error in e.exception]
        self.assertEqual(len(fields), 1)
        self.assertIn("name", fields)
        # Musician
        with self.assertRaises(ValidationError) as e:
            self.musician.objects.create()
        fields = [error[0] for error in e.exception]
        self.assertEqual(len(fields), 4)
        self.assertIn("name", fields)
        self.assertIn("nationality", fields)
        self.assertIn("instrument", fields)
        self.assertIn("author", fields)

    def test_year_of_release(self):
        """Test the year field."""
        params = self.album_params.copy()
        # Test year lower than 1000
        params["year_of_release"] = 999
        with self.assertRaises(ValidationError) as e:
            self.album.objects.create(**params)
        fields = [error[0] for error in e.exception]
        self.assertIn("year_of_release", fields)
        # Test year in the future
        params["year_of_release"] = datetime.today().year + 1
        with self.assertRaises(ValidationError) as e:
            self.album.objects.create(**params)
        fields = [error[0] for error in e.exception]
        self.assertIn("year_of_release", fields)

    def test_string_lengths(self):
        """Test the maximum length of strings."""
        params = self.musician_params.copy()
        params["name"] = "a" * 151
        with self.assertRaises(ValidationError) as e:
            self.musician.objects.create(**params)
        fields = [error[0] for error in e.exception]
        self.assertIn("name", fields)

    def test_first_and_last_appearance(self):
        """Test the year field."""
        params = self.author_params.copy()
        # Test year lower than 1000
        params["first_appearance"] = 999
        params["last_appearance"] = 999
        with self.assertRaises(ValidationError) as e:
            self.author.objects.create(**params)
        fields = [error[0] for error in e.exception]
        self.assertIn("first_appearance", fields)
        self.assertIn("last_appearance", fields)
        # Test year in the future
        params["first_appearance"] = datetime.today().year + 1
        params["last_appearance"] = datetime.today().year + 1
        with self.assertRaises(ValidationError) as e:
            self.author.objects.create(**params)
        fields = [error[0] for error in e.exception]
        self.assertIn("first_appearance", fields)
        self.assertIn("last_appearance", fields)

    def test_removed_fields(self):
        """Test removed fields in the Song model."""
        fields = [field.name for field in self.song._meta.get_fields()]
        self.assertNotIn("author_website", fields)

    def test_foreign_keys(self):
        """Test the foreign keys."""
        fields = [
            self.song._meta.get_field("author"),
            self.song._meta.get_field("album"),
            self.musician._meta.get_field("author"),
        ]
        for field in fields:
            self.assertTrue(isinstance(field, db.models.ForeignKey))
