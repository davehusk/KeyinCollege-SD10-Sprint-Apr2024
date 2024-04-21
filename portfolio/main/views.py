from django.shortcuts import render, get_object_or_404
from .models import Project, Tag

# home view
def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, "home.html", {"projects": projects, "tags": tags})

# contact page
def contact(request):
    return render(request, "contact.html")

# project page
def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {"project": project})
