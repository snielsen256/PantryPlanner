from django.urls import path
from . import views

urlpatterns = [
    path("", views.find_recipes),
    path("find_forgotten_recipe/search", views.search)
]