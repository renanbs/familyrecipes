from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Recipe
# Create your views here.


class RecipesList(View):
    template_name = "recipes_list.html"

    def get(self, request):
        recipes = Recipe.objects.all()
        context = {
            "title": "Recipes",
            "recipes": recipes
        }
        return render(request, self.template_name, context)


class RecipeDetail(View):
    template_name = "recipe.html"

    def get(self, request, id):

        recipe = get_object_or_404(Recipe, id=id)
        ingredients = recipe.ingredients.all()
        print(ingredients)
        context = {
            "recipe": recipe,
            "ingredients": ingredients,
        }
        return render(request, self.template_name, context)
