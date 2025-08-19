from datetime import timedelta
from pathlib import Path

from django import db
from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.files import File
from django.test import TestCase

BASE_DIR = Path(__file__).resolve().parent


class Task1(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = get_user_model()
        cls.song = cls.get_model(cls, "Song")
        cls.profile = cls.get_model(cls, "Profile")

    def setUp(self):
        """Set up."""
        self.profile_params = {
            "user": 1,
            "preferred_style": "Pop"
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
        self.assertIsNotNone(self.song)
        self.assertIsNotNone(self.profile)

    def test_new_fields(self):
        """Test new fields in the Song model."""
        fields = [field.name for field in self.song._meta.get_fields()]
        self.assertIn("created_by", fields)
        self.assertIn("last_modified_by", fields)

    def test_required_fields(self):
        """Test the required fields."""
        # Song
        with self.assertRaises(ValidationError) as e:
            self.song.objects.create()
        fields = [error[0] for error in e.exception]
        self.assertNotIn("created_by", fields)
        self.assertNotIn("last_modified_by", fields)
        # Profile
        with self.assertRaises(ValidationError) as e:
            self.profile.objects.create()
        fields = [error[0] for error in e.exception]
        self.assertEqual(len(fields), 2)
        self.assertIn("user", fields)
        self.assertIn("preferred_style", fields)

    def test_foreign_keys(self):
        """Test the foreign keys."""
        fields = [
            (self.song._meta.get_field("created_by"), self.user),
            (self.song._meta.get_field("last_modified_by"), self.user),
            (self.profile._meta.get_field("preferred_song"), self.song),
        ]
        for field in fields:
            # Check the field type
            self.assertTrue(isinstance(field[0], db.models.ForeignKey))
            # Check the model referenced
            self.assertTrue(field[0].remote_field.model is field[1])

    def test_one_to_one(self):
        """Test the one to one fields."""
        fields = [
            (self.profile._meta.get_field("user"), self.user),
        ]
        for field in fields:
            # Check the field type
            self.assertTrue(isinstance(field[0], db.models.OneToOneField))
            # Check the model referenced
            self.assertTrue(field[0].remote_field.model is field[1])
