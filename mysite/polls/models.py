from django.db import models


class Drink(models.Model):
    drink_name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    ingredient = models.ManyToManyField('Ingredient', through='IngredientRatio')

    def __str__(self):
        return self.drink_name


class Ingredient(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class IngredientRatio(models.Model):
    quantity = models.DecimalField(max_digits=4, decimal_places=2, unique=True)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    def __str__(self):
        return "{0}: {1} : {2}".format(self.drink, self.ingredient.name, self.quantity)


class TankAllocation(models.Model):
    name = models.CharField(max_length=8, unique=True)
    allocation = models.ForeignKey('Ingredient', on_delete=models.CASCADE, default='NULL', related_name='ingredients')

    def __str__(self):
        return "{0}: {1}".format(self.allocation.name, self.name)
