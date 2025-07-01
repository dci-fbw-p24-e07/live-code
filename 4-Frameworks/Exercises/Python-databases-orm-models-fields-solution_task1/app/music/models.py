from django.db import models
from django.core.exceptions import ValidationError


def less_than_five(value):
    """Raire an error if the value is 5 or greater."""
    if value >= 5:
        raise ValidationError("The price must be lower than 5 euros.")


class Song(models.Model):
    """The Song model."""

    STYLES = (
        ("Indie", "Indie"),
        ("Pop", "Pop"),
        ("Rock", "Rock"),
        ("Funky", "Funky"),
        ("Reggaeton", "Reggaeton"),
        ("Classic", "Classic"),
        ("Orquestra", "Orquestra"),
        ("Folk", "Folk"),
    )

    audio = models.FileField(upload_to="audio")
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=50, db_index=True, null=True, blank=True)
    author_website = models.URLField(null=True, blank=True)
    album = models.CharField(max_length=250, null=True, blank=True)
    duration = models.DurationField()
    style = models.CharField(max_length=20, choices=STYLES, null=True, blank=True)
    playbacks = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=3, validators=[less_than_five],
                                default=0)
    deal_of_the_day = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """Validate the model when saving."""
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        """Metadata."""

        constraints = [
            models.UniqueConstraint(fields=["title", "author", "album",
                                            "duration"],
                                    name="unique_song")
        ]

# Task 2
from django.db import models
from django.core.exceptions import ValidationError


def less_than_five(value):
    """Raire an error if the value is 5 or greater."""
    if value >= 5:
        raise ValidationError("The price must be lower than 5 euros.")


class Audio(models.Model):
    """The Audio model."""

    SONG_STYLES = (
        ("Indie", "Indie"),
        ("Pop", "Pop"),
        ("Rock", "Rock"),
        ("Funky", "Funky"),
        ("Reggaeton", "Reggaeton"),
        ("Classic", "Classic"),
        ("Orquestra", "Orquestra"),
        ("Folk", "Folk")
    )

    TYPES = (
        ("song", "Song"),
        ("podcast", "Podcast"),
        ("effect", "Effect")
    )

    audio = models.FileField(upload_to="audio")
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=50, db_index=True, null=True, blank=True)
    author_website = models.URLField(null=True, blank=True)
    album = models.CharField(max_length=250, null=True, blank=True)
    duration = models.DurationField()
    type = models.CharField(max_length=10, choices=TYPES)
    song_style = models.CharField(max_length=20, choices=SONG_STYLES, null=True, blank=True)
    playbacks = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    deal_of_the_day = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """Validate the model when saving."""
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        """Validate accross fields."""
        if self.type != "song" and self.song_style is not None:
            raise ValidationError("Only songs may have an associated style.")
        if self.price:
            if self.type == "song" and self.price >= 5:
                raise ValidationError("The price of a song must be lower than 5 euros.")
            if self.type == "podcast" and self.price >= 4:
                raise ValidationError("The price of a podcast must be lower than 4 euros.")
            if self.type == "effect" and self.price >= 95:
                raise ValidationError("The price of an audio effect must be lower than 100 euros.")

    class Meta:
        """Metadata."""

        constraints = [
            models.UniqueConstraint(fields=["title", "author", "album",
                                            "duration"],
                                    name="unique_song")
        ]