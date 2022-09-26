from django.shortcuts import render


def projects(request):
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context = {"number": number}
    return render(request, "projects/projects.html", context)


def single_project(request, pk):
    return render(request, "projects/single-project.html")
