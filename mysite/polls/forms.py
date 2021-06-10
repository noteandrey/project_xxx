from django import forms


class DrinkSearchForm(forms.Form):
    name = forms.CharField(label='Nazwa drinka', max_length=100)
