from django.test import TestCase
import time
from django.apps import apps
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.db import transaction
from pathlib import Path
from django.core.files import File

BASE_DIR = Path(__file__).resolve().parent


class Task1(TestCase):

    model_name = "Audio"
    model = None
    basic_params = None

    def setUp(self):
        """Set up."""
        self.model = self.get_model()
        audio = open(BASE_DIR / "sample.mp3", "rb")
        self.basic_params = {
            "audio": File(audio, name="sample.mp3"),
            "title": "Test sample",
            "duration": timedelta(seconds=27),
            "type": "song"
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
        self.assertIn("type", fields)

    def test_positive_integers(self):
        """Test the positive integer fields."""
        params = self.basic_params.copy()
        params["playbacks"] = -1
        with self.assertRaises(ValidationError) as e:
            self.model.objects.create(**params)
        fields = [error[0] for error in e.exception]
        self.assertIn("playbacks", fields)

    def test_type(self):
        """Test the type field."""
        # A type field exists
        params = self.basic_params.copy()
        obj = self.model.objects.create(**params)
        self.assertTrue(hasattr(obj, "type"))
        # It only allows song, podcast or effect.
        choices = [choice[0] for choice in self.model._meta.get_field("type").choices]
        self.assertEqual(len(choices), 3)
        self.assertIn("song", choices)
        self.assertIn("podcast", choices)
        self.assertIn("effect", choices)
        # Make sure the validation works
        params["type"] = "audiobook"
        with self.assertRaises(ValidationError):
            self.model.objects.create(**params)

    def test_style(self):
        """Test the style field."""
        params = self.basic_params.copy()
        # The song_style allows values when the type is song
        params.update({"type": "song", "song_style": "Funky"})
        try:
            obj = self.model.objects.create(**params)
        except Exception:
            obj = None
        self.assertIsInstance(obj, self.model)
        # No style is allowed when the type is podcast
        params.update({"title": "Test podcast", "type": "podcast", "song_style": "Funky"})
        with self.assertRaises(ValidationError):
            obj = self.model.objects.create(**params)
        # No style is allowed when the type is effect
        params.update({"title": "Test effect", "type": "effect", "song_style": "Funky"})
        with self.assertRaises(ValidationError):
            obj = self.model.objects.create(**params)

    def test_price(self):
        """Test the price validation."""
        # Test the default value
        params = self.basic_params.copy()
        obj = self.model.objects.create(**params)
        self.assertEqual(obj.price, 0)
        # Test price validation for a song
        params["price"] = 5
        params["title"] = "Test song price"
        with self.assertRaises(ValidationError) as e:
            self.model.objects.create(**params)
        # Test price validation for a podcast
        params["price"] = 4
        params["type"] = "podcast"
        params["title"] = "Test podcast price"
        with self.assertRaises(ValidationError) as e:
            self.model.objects.create(**params)
        # Test price validation for an effect
        params["price"] = 95
        params["type"] = "effect"
        params["title"] = "Test effect price"
        with self.assertRaises(ValidationError) as e:
            self.model.objects.create(**params)

    def test_notes(self):
        """Make sure the notes field does not exist."""
        with self.assertRaises(AttributeError) as e:
            obj = self.model.objects.create(**self.basic_params)
            notes = obj.notes

    def test_auto_timestamps(self):
        """Test the created and last_modified."""
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
