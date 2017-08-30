from django.db import models

# Create your models here.


class Unit(models.Model):
    unit = models.CharField(max_length=100)

    def __str__(self):
        return self.unit

    class Meta:
        ordering = ['unit']


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit = models.ForeignKey(Unit)

    def __str__(self):
        return self.name

