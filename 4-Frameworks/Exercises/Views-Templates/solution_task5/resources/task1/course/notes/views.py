"""Views for the notes app."""
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

from notes.models import notes


def redirect_to_note_detail(request, note_id):
    """Redirect to the note details view."""
    return redirect(reverse("notes:details", args=[note_id]))


def home(request):
    """Home for my notes app."""
    response = [
        "<h1>Welcome to my course notes!</h1>",
        "<a href=\"", reverse("notes:sections"), "\">Check the list of sections</a>", " | ",
        "<a href=\"", reverse("notes:details", args=[1]), "\">Read my first note</a>",
    ]
    return HttpResponse("".join(response))


def _get_section_list_item(text):
    """Return the list item for a section."""
    url = reverse("notes:by_section", args=[text])
    link = f"<a href=\"{url}\">{text}</a>"
    return f"<li>{link}</li>"


def sections(request):
    """Show the list of note sections."""
    response = [
        "<h1>Browse my notes by section</h1>",
        "<ol>",
        _get_section_list_item("Web Frameworks"),
        _get_section_list_item("Setting up Django"),
        _get_section_list_item("URL Mapping"),
        "</ol>",
        "<a href=\"", reverse("notes:home"), "\">Back to home</a>"
    ]
    return HttpResponse("".join(response))


def by_section(request, section_name):
    """Show the notes of a section."""
    response = [
        f"<h1>Notes about {section_name}</h1>",
        "<ol>"]
    response = response + _get_note_items_by_section(section_name)
    response = response + [
        "</ol>",
        "<a href=\"", reverse("notes:sections"), "\">Back to sections</a>"
    ]
    return HttpResponse("".join(response))


def _get_note_items_by_section(section_name):
    """Return the notes of a section as list items."""
    return [f"<li>{note['text']}</li>" for note in notes
            if note["section"] == section_name]


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


def details(request, note_id):
    """Show a single note matching the note_id."""
    note = notes[note_id - 1]
    previous_note = "Previous note"
    next_note = "Next note"
    if note_id - 1 > 0:
        previous_url = reverse("notes:details", args=[note_id - 1])
        previous_note = f"<a href=\"{previous_url}\">Previous note</a>"
    if note_id < len(notes):
        next_url = reverse("notes:details", args=[note_id + 1])
        next_note = f"<a href=\"{next_url}\">Next note</a>"
    response = [
        f"<h1>Note number {note_id}</h1>",
        "<h3>", note["section"], "</h3>",
        "<p>", note["text"], "<p>",
        previous_note, " | ",
        "<a href=\"", reverse("notes:home"), "\">Back to home</a>", " | ",
        next_note
    ]
    return HttpResponse("".join(response))


def _get_note_items_matching_search(search_term):
    """Return a list of items with notes marching the search."""
    return [f"<li>{note['text']}</li>" for note in notes
            if search_term.lower() in note["text"].lower()]
