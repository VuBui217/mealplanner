from django.contrib import admin
from .models import Recipe, MealPlan, MealPlanRecipe
# Register your models here.
admin.site.register(Recipe)
admin.site.register(MealPlan)
admin.site.register(MealPlanRecipe)

