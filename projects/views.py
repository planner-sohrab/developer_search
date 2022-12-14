from django.shortcuts import redirect, render
from .models import Project, Tag
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)


def single_project(request, pk):
    project = Project.objects.get(id=pk)
    # tag = Tag.objects.get(id=project.id)
    context = {"project": project}
    return render(request, "projects/single-project.html", context)


def create_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("projects")
    context = {"form": form}
    return render(request, "projects/project_form.html", context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")
    context = {"form": form, "project": project}
    return render(request, "projects/update_project.html", context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")

    context = {"project": project}
    return render(request, "projects/delete_project.html", context)
