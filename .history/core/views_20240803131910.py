from django.shortcuts import render
from django.views.generic import View


class Index(View):
    template_name = 'index.html'
