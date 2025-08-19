"""Notes URL Configuration."""
from django.urls import path

from notes.views import NotesBySection, details, home, search, SectionList

app_name = "notes"
urlpatterns = [
    path('', home, name="home"),
    path('sections/', SectionList.as_view(), name="sections"),
    path('sections/<section_name>/', NotesBySection.as_view(), name="by_section"),
    path('<int:note_id>/', details, name="details"),
    path('<str:search_term>/', search, name="search"),
]
