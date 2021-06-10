from django.shortcuts import render, get_object_or_404
from .models import Ingredient, IngredientRatio, Drink, TankAllocation
from django.views import generic, View
from .forms import DrinkSearchForm

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


def details(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    context = {
        'drink': drink,
    }
    return render(request, 'polls/drink_detail.html', context)


class DrinkSearchView(View):

    def get(self, request):
        form = DrinkSearchForm()
        ctx = {
            'form': form,
        }
        return render(request, 'polls/drink_search.html', ctx)

    def post(self, request):
        form = DrinkSearchForm(request.POST)
        if form.is_valid():
            drinks = Drink.objects.filter(drink_name__contains=form.cleaned_data['name'])
            ctx = {
                'form': form,
                'drinks': drinks,
            }
            return render(request, 'polls/drink_search.html', ctx)
        else:
            error = "Złe dane formularza"
            ctx = {
                'form': form,
                'error ': error,
            }
            return render(request, 'polls/drink_search.html', ctx)
