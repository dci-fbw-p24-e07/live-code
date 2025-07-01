import time
from datetime import datetime, timedelta
from pathlib import Path

from django.apps import apps
from django.core.exceptions import ValidationError
from django.core.files import File
from django.test import TestCase

BASE_DIR = Path(__file__).resolve().parent


class Task1(TestCase):

    model_name = "Song"
    model = None
    basic_params = None

    def setUp(self):
        """Set up."""
        self.model = self.get_model()
        audio = open(BASE_DIR / "sample.mp3", "rb")
        self.basic_params = {
            "audio": File(audio, name="sample.mp3"),
            "title": "Test sample",
            "duration": timedelta(seconds=27)
        }
        super().setUpClass()

    def tearDown(self):
        """Remove uploaded files."""
        audios = []
        for song in self.model.objects.all():
            audios.append(song.audio)
            song.delete()
        try:
            for audio in audios:
                audio.delete()
        except ValidationError:
            pass

    def get_model(self):
        """Return the model if it exists."""
        try:
            model = apps.get_model("music", self.model_name)
        except LookupError:
            model = None
        return model

    def test_model_name(self):
        """Test the name of the model."""
        self.assertIsNotNone(self.model)

    def test_required_fields(self):
        """Test the required fields."""
        with self.assertRaises(ValidationError) as e:
            self.model.objects.create()
        fields = [error[0] for error in e.exception]
        self.assertIn("audio", fields)
        self.assertIn("title", fields)
        self.assertIn("duration", fields)

    def test_positive_integers(self):
        """Test the positive integer fields."""
        params = self.basic_params.copy()
        params["playbacks"] = -1
        with self.assertRaises(ValidationError) as e:
            self.model.objects.create(**params)
        fields = [error[0] for error in e.exception]
        self.assertIn("playbacks", fields)

    def test_price(self):
        """Test the price validation."""
        # Test the default value
        params = self.basic_params.copy()
        obj = self.model.objects.create(**params)
        self.assertEqual(obj.price, 0)
        # Test price validation
        params["price"] = 5
        with self.assertRaises(ValidationError) as e:
            self.model.objects.create(**params)
        fields = [error[0] for error in e.exception]
        self.assertIn("price", fields)

    def test_auto_timestamps(self):
        """Test the created and last_updated."""
        # Test the creation of a new object
        params = self.basic_params.copy()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        obj = self.model.objects.create(**params)
        self.assertEqual(obj.created.strftime("%Y-%m-%d %H:%M:%S"), now)
        self.assertEqual(obj.last_modified.strftime("%Y-%m-%d %H:%M:%S"), now)
        # Test the updating of an old object
        time.sleep(1)
        obj.title = "Test timestamps"
        obj.save()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertNotEqual(obj.created.strftime("%Y-%m-%d %H:%M:%S"), now)
        self.assertEqual(obj.last_modified.strftime("%Y-%m-%d %H:%M:%S"), now)

    def test_unique_constraint(self):
        """Test the unique constraint."""
        params = self.basic_params.copy()
        params["author"] = "Test author"
        params["album"] = "Test album"
        with self.assertRaises(ValidationError) as e:
            self.model.objects.create(**params)
            self.model.objects.create(**params)
        fields = [error[0] for error in e.exception]
        self.assertIn("__all__", fields)
