from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer
from datetime import date

# Create your views here.
class GenerateMealPlan(APIView):
    def post(self, request):
        weight = request.data.get('weight')
        height = request.data.get('height')
        goal = request.data.get('goal')
        cuisine = request.data.get('cuisine')

        calories = 2000 if goal == 'maintain' else 1800 if goal =='lose' else 2200
        recipes = Recipe.objects.filter(cuisine=cuisine, calories__lte = calories)
        serializer = RecipeSerializer(recipes, many=True)

        return Response({
            'calories': calories,
            'recipes': serializer.data,
            'week_start': date.today()
        })
