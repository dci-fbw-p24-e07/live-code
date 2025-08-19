"""Custom template tags and filters."""

from django import template
from django.urls import reverse

register = template.Library()


@register.filter
def linked_section(section_name):
    """Return the section_name as a link."""
    link = [
        "<a href=\"",
        reverse("notes:by_section", args=[section_name]),
        "\">",
        section_name,
        "</a>"
    ]
    return "".join(link)
