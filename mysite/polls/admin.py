from django.contrib import admin
from .models import Ingredient, IngredientRatio, Drink, TankAllocation


class IngredientRatioAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'ingredient', 'drink')
    list_filter = ('ingredient', 'drink')
    fields = ['ingredient', 'drink', ('quantity')]


admin.site.register(Drink)
admin.site.register(Ingredient)
admin.site.register(IngredientRatio, IngredientRatioAdmin)
admin.site.register(TankAllocation)