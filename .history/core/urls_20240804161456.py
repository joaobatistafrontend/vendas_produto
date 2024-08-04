from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexMes.as_view()),
    path('detalhes/', IndexMes.as_view()),
]
