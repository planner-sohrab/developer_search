from django.urls import path
from .views import (
    projects,
    single_project,
    create_project,
    update_project,
    delete_project,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("projects", projects, name="projects"),
    path("project/<str:pk>", single_project, name="single_project"),
    path("create_project", create_project, name="create_project"),
    path("update_project/<str:pk>", update_project, name="update_project"),
    path("delete_project/<str:pk>", delete_project, name="delete_project"),
    # path("update_project", update_project, name="update_project"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
