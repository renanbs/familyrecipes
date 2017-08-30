from django.shortcuts import render
from django.views import View

from .models import Ingredient
# Create your views here.


class IngredientsList(View):
    template_name = "recipes_list.html"

    def get(self, request):
        ingredients = Ingredient.objects.all()
        context = {
            "title": "Ingredients",
            "recipes": ingredients
        }
        return render(request, self.template_name, context)