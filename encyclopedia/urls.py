from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("results", views.results, name="results"),
    path("new_page", views.new_page, name="new_page"),
    path("<str:title>", views.title, name="title"),
    path("<str:title>/edit", views.edit, name="edit")
]
