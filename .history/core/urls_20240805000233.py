from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexMes.as_view()),
    path('detalhesDias/', DetalhesDias.as_view(), name='detalhesDias'),
    path('detalhesSemanas/', DetalhesDias.as_view(), name='detalhesSemana'),
]
