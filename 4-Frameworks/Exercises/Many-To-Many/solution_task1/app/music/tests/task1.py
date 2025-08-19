from datetime import timedelta
from pathlib import Path

from django import db
from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.core.files import File
from django.test import TestCase

BASE_DIR = Path(__file__).resolve().parent


class Task1(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = get_user_model()
        cls.author = cls.get_model(cls, "Author")
        cls.musician = cls.get_model(cls, "Musician")
        cls.song = cls.get_model(cls, "Song")

    def setUp(self):
        """Set up."""
        self.author_params = {
            "name": "Test author"
        }
        self.musician_params = {
            "name": "Test musician",
            "instrument": "sax",
            "nationality": "DE"
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
        self.assertIsNotNone(self.author)
        self.assertIsNotNone(self.musician)

    def test_many_to_many(self):
        """Test the many_to_many relationships."""
        # Musician <--> Author
        matches = False
        for field in self.musician._meta.get_fields():
            if isinstance(field, db.models.ManyToManyField) and field.related_model is self.author:
                matches = True
        self.assertTrue(matches)
        # Song <--> Author
        matches = False
        for field in self.song._meta.get_fields():
            if isinstance(field, db.models.ManyToManyField) and field.related_model is self.author:
                matches = True
        self.assertTrue(matches)
        # Check if it is a custom through table with not-null start
        musician = self.musician.objects.create(**self.musician_params)
        author = self.author.objects.create(**self.author_params)
        with self.assertRaises(IntegrityError) as e:
            musician.authors.add(author)
        self.assertIn("not-null constraint", str(e.exception))
        self.assertIn("start", str(e.exception))

    def test_through_fields(self):
        musician = self.musician.objects.create(**self.musician_params)
        author = self.author.objects.create(**self.author_params)
        self.musician.authors.through.objects.create(
            musician=musician, author=author, start=1997, end=2000)
        self.assertEqual(musician.authors.count(), 1)
        self.assertEqual(author.members.count(), 1)
