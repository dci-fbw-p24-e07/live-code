"""Notes URL Configuration."""
from django.urls import path

from notes.views import NotesBySection, NoteDetails, home, SearchResultsView, SectionList

app_name = "notes"
urlpatterns = [
    path('', home, name="home"),
    path('sections/', SectionList.as_view(), name="sections"),
    path('sections/<section_name>/', NotesBySection.as_view(), name="by_section"),
    path('<int:note_id>/', NoteDetails.as_view(), name="details"),
    path('<str:search_term>/', SearchResultsView.as_view(), name="search"),
]
