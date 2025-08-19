"""Todo views."""
from django.http import HttpResponse
from django.urls import reverse

from todo.models import todos


def details(request, todo_id):
    """Show a single todo matching the todo_id."""
    todo = todos[todo_id - 1]
    previous = "Previous todo"
    next = "Next todo"
    if todo_id - 1 > 0:
        previous_url = reverse("todo:details", args=[todo_id - 1])
        previous = f"<a href=\"{previous_url}\">Previous todo</a>"
    if todo_id < len(todos):
        next_url = reverse("todo:details", args=[todo_id + 1])
        next = f"<a href=\"{next_url}\">Next todo</a>"
    response = [
        f"<h1>To Do number {todo_id}</h1>",
        "<h3>", todo["topic"], "</h3>",
        "<p>", todo["text"], "<p>",
        "<p>", todo["status"].capitalize(), "</p>",
        previous, " | ",
        next
    ]
    return HttpResponse("".join(response))
