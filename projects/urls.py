from django.urls import path
from .views import projects, single_project

urlpatterns = [
    path("projects", projects),
    path("project/<str:pk>", single_project),
]
