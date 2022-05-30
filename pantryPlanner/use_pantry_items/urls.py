from django.urls import path
from . import views

urlpatterns = [
    path("", views.find_recipes),
    path("use_pantry_items/search", views.search)
]