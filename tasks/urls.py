from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("alina", views.alina, name="alina"),
  path("<str:name>", views.greet, name="greet"),
]
