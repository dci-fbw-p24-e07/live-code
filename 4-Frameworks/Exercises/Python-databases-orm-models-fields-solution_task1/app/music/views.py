from music.models import Audio
from datetime import timedelta
from django.db.models import Q


def subtask1():
    return Audio.objects.filter(type="song")


def subtask2():
    return Audio.objects.filter(type="podcast").count()


def subtask3():
    return Audio.objects.exclude(type="song").count()


def subtask4():
    return Audio.objects.filter(type="song").order_by("duration")[:10]


def subtask5():
    return Audio.objects.filter(type="effect").order_by("-price")[2]


def subtask6():
    some_songs = Audio.objects.filter(
        type="song",
        duration__gte=timedelta(minutes=2),
        duration__lte=timedelta(minutes=3)
    )
    return some_songs.count()


def subtask7():
    return Audio.objects.filter(
        Q(type="song"),
        Q(duration__gte=timedelta(minutes=2), duration__lte=timedelta(minutes=3)) | Q(price__gte=2)
    ).count()


def subtask8():
    return Audio.objects.filter(
        type="podcast",
        duration__gt=timedelta(minutes=30)
    ).update(price=3.99)
    