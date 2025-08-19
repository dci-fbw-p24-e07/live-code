"""Notes URL Configuration."""
from django.urls import path

from notes.views import by_section, details, home, search, sections

app_name = "notes"
urlpatterns = [
    path('', home, name="home"),
    path('sections/', sections, name="sections"),
    path('sections/<section_name>/', by_section, name="by_section"),
    path('<int:note_id>/', details, name="details"),
    path('<str:search_term>/', search, name="search"),
]
