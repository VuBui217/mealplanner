from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    cuisine = models.CharField(max_length=50)
    calories = models.IntegerField()
    meal_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    week_start = models.DateField()
    created_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Meal plan for {self.user} starting {self.week_start}"
    
class MealPlanRecipe(models.Model):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    day = models.IntegerField()
    meal_slot = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.meal_slot} on day {self.day}: {self.recipe.name}"