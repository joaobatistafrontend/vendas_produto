from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexMes.as_view()),
    path('detalhes/', DetalhesDias.as_view(), name='detalhesDias'),
    path('detalhes/', DetalhesDias.as_view(), name='detalhesDias'),
]
