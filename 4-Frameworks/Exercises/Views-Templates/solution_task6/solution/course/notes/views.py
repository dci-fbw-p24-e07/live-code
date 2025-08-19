"""Views for the notes app."""
from django.template.loader import get_template
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from notes.models import notes


def redirect_to_note_detail(request, note_id):
    """Redirect to the note details view."""
    return redirect(reverse("notes:details", args=[note_id]))


def home(request):
    """Home for my notes app."""
    template = get_template("notes/home.html")
    context = {
        "title": "Welcome to my course notes!",
        "links": [
            {
                "url": reverse("notes:sections"),
                "label": "Check the list of sections"
            },
            {
                "url": reverse("notes:details", args=[1]),
                "label": "Read my first notes"
            }
        ]
    }
    return HttpResponse(template.render(context))


class SectionList(TemplateView):
    """List of sections."""

    template_name = "notes/sections.html"

    def get_context_data(self):
        """Return the list of sections."""
        return {
            "sections": ["Web Frameworks",
                         "Setting up Django",
                         "URL Mapping"]
            }


class NotesBySection(TemplateView):
    """Show the notes of a section."""

    template_name = "notes/by_section.html"

    def get_context_data(self, section_name):
        """Return the section name and the note list."""
        return {
            "section": section_name,
            "notes": _get_notes_by_section(section_name)
        }


def _get_notes_by_section(section_name):
    """Return the notes of a section."""
    return [note for note in notes
            if note["section"] == section_name]


class SearchResultsView(TemplateView):
    """Execute the search and show results."""

    template_name = "notes/search.html"

    def get_context_data(self, search_term):
        """Return the term and list of notes."""
        return {
            "notes": notes,
            "term": search_term
        }


def search(request, search_term):
    """Show a list of all notes matching the search."""
    response = [
        f"<h1>Notes matching {search_term}</h1>",
        "<ol>"]
    response = response + _get_note_items_matching_search(search_term)
    response = response + [
        "</ol>",
        "<a href=\"", reverse("notes:home"), "\">Back to home</a>"
    ]
    return HttpResponse("".join(response))


class NoteDetails(TemplateView):
    """Note details."""

    template_name = "notes/details.html"

    def get_context_data(self, note_id):
        """Return the note data."""
        return {
            "id": note_id,
            "num_notes": len(notes),
            "note": notes[note_id - 1]
        }


def _get_note_items_matching_search(search_term):
    """Return a list of items with notes marching the search."""
    return [f"<li>{note['text']}</li>" for note in notes
            if search_term.lower() in note["text"].lower()]
