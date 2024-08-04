from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexMes.as_view()),
    path('detalhes/int:id', IndexMes.as_view()),
]
