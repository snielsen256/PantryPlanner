from django.shortcuts import render
from django.http import HttpResponse

def find_recipes(request):
    return render(request, "use_pantry_items.html")

def search(request):
    #searches recipeData for a recipe containing that ingredient
    search_param = request.POST.get("textfield", None)
    found_recipes = []
    
    for chosen_recipe in recipeData:
        for ingredient_num in range(len(chosen_recipe["ingredients"])):

            if search_param.lower() in chosen_recipe["ingredients"][ingredient_num]:
                found_recipes.append([chosen_recipe["Name"], chosen_recipe["Site"]])
    
    if len(found_recipes) == 0:
        return HttpResponse("None Found")
    else:
        return render(request, "use_pantry_items.html", {"recipes": found_recipes})


# A basic database for testing.
recipeData = [
    {
        "Name": "Crusty Sourdough Dinner Rolls, no-knead, no added yeast",
        "Site": "https://holycowvegan.net/crusty-sourdough-dinner-rolls-no-knead-and-no-added-yeast/",
        "ingredients": [
            "bread flour",
            "warm filtered or distilled water",
            "salt",
            "sourdough starter"
        ]
    },
    {
        "Name": "Teriyaki Chicken",
        "Site": "https://cafedelites.com/wprm_print/49653",
        "ingredients": [
            "skinless boneless chicken thighs",
            "cooking oil",
            "low-sodium soy sauce",
            "cooking sake",
            "Mirin",
            "sesame oil",
            "minced garlic",
            "shallot/green onion stem",
            "broccoli florets",
            "cornstarch"
        ]
    },
    {
        "Name": "Crepes",
        "Site": "https://www.allrecipes.com/recipe/27188/crepes/",
        "ingredients": [
            "eggs",
            "milk",
            "all-purpose flour",
            "salt",
            "vegetable oil"
        ]
    },
    {
        "Name": "Rice Cooker Rice Pudding",
        "Site": "https://www.allrecipes.com/recipe/228474/rice-cooker-rice-pudding/",
        "ingredients": [
            "skim milk",
            "short-grain white rice",
            "white sugar",
            "ground cinnamon"

        ]
    },
    {
        "Name": "Congee",
        "Site": "https://www.allrecipes.com/recipe/258062/congee/",
        "ingredients": [
            "chicken stock",
            "water",
            "white rice",
            "apple cider vinegar",
            "fish sauce",
            "grated fresh ginger",
            "salt",
            "sesame oil",
            "lean white fish",
            "pickled chinese vegetables",
            "chinese roast pork",
            "chopped scallions",
            "crushed peanuts",
            "vinegar",
            "soy sauce",
        ]
    },
]