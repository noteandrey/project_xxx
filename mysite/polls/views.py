from django.shortcuts import render, get_object_or_404
from .models import Ingredient, IngredientRatio, Drink, TankAllocation
from django.views import generic



def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_drink=Drink.objects.all().count()
    num_ingredient=Ingredient.objects.all().count()
    num_ingredient_available=Ingredient.objects.all().count()
    num_ingredient_ratio=IngredientRatio.objects.count()  # Метод 'all()' применён по умолчанию.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_drink':num_drink,'num_ingredient':num_ingredient,'num_ingredient_available':
            num_ingredient_available,'num_ingredient_ratio':num_ingredient_ratio,'num_visits':num_visits},
    )


class DrinkListView(generic.ListView):
    model = Drink
    paginate_by = 5


class DrinkDetailView(generic.DetailView):
    model = Drink
