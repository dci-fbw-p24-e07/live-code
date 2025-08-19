"""ToDo URL Configuration."""
from django.urls import path

from todo.views import details

app_name = "todo"
urlpatterns = [
    path('<int:todo_id>/', details, name="details"),
]
