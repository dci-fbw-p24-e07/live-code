from django.urls import path, include
from rest_framework import routers
from . import views

app_name = "blog"

# Initialize the router object
router = routers.SimpleRouter()

# Register the endpoints and Views
router.register(r'tasks', views.TaskViewSet, basename="tasks")

urlpatterns = [
    path("", views.BlogPostListCreate.as_view()),
    path("", include(router.urls))
]
