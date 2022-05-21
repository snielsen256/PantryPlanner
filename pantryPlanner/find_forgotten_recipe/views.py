from django.shortcuts import render
from django.http import HttpResponse

def find_recipes(request):


    return render(request, "find_forgotten_recipe.html", {"name": "Stevp"})