from django.db import models
from django.core.urlresolvers import reverse

from ingredients.models import Ingredient

# Create your models here.


class Recipe(models.Model):
    # slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    ingredients = models.ManyToManyField(Ingredient)
    preparation_mode = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"id": self.id})

