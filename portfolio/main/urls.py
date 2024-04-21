from django.urls import path
from . import views

# URL endpoints. It's only a boilerplate for now.
urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("project/<int:id>/", views.project, name="project"),
]
