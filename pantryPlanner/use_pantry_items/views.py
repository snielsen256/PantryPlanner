from django.shortcuts import render
from django.http import HttpResponse

def find_recipes(request):


    return render(request, "use_pantry_items.html", {"name": "Stepv"})

