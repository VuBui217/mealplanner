import os
import django
import sys
import requests
from dotenv import load_dotenv
#sys.path.append('/Users/tacmeics/Desktop/mealplanner/backend')  # path where manage.py is
load_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mealplanner.settings')
django.setup()
from meals.models import Recipe
API_KEY = os.getenv('SPOONACULAR_API_KEY')
BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

def import_recipes(cuisine='Italian', max_recipes = 10):
    params = {
        "apiKey": API_KEY,
        "cuisine": cuisine,
        "number": max_recipes,
        "addRecipeNutrition": True,
        "instructionsRequired": True
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        print("API Response:", response.json())  # Debug: Print raw response
    except requests.RequestException as e:
        print(f"Error fetching recipes: {e}")
        return

    recipes = response.json().get("results", [])
    if not recipes:
        print(f"No recipes found for cuisine: {cuisine}")
        return

    imported_count = 0
    for recipe in recipes:
        nutrition = recipe.get("nutrition", {})
        calories = next(
            (n["amount"] for n in nutrition.get("nutrients", []) if n["name"] == "Calories"),
            0
        )
        if calories == 0:
            print(f"Skipping recipe '{recipe.get('title')}' due to zero calories")
            continue

        dish_types = recipe.get("dishTypes", [])
        meal_type = next(
            (dt for dt in dish_types if dt in ["breakfast", "lunch", "dinner"]),
            "Unknown"
        )
        
        Recipe.objects.create(
            name=recipe["title"],
            ingredients=", ".join([ing["name"] for ing in recipe.get("extendedIngredients", [])]),
            instructions=recipe.get("instructions") or "No instructions provided",
            cuisine=cuisine,
            calories=int(calories),
            meal_type=meal_type
        )
        
        imported_count += 1
    print(f"Imported {imported_count} recipes")

#if __name__ == "__main__":
 #   import_recipes()
import_recipes(cuisine='Italian', max_recipes = 10)