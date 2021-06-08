from django.urls import path, include
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^drink/$', views.DrinkListView.as_view(), name='drink'),
    url(r'^drink/(?P<pk>\d+)$', views.DrinkDetailView.as_view(), name='drink-detail'),
]