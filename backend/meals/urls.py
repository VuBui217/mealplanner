from django.urls import path
from .views import GenerateMealPlan

urlpatterns = [
    path('generate-meal-plan/', GenerateMealPlan.as_view(), name= 'generate-meal-plan'), #http://localhost:8000/api/generate-meal-plan/

]