from django.shortcuts import render
from django.views.generic import View,TemplateView


class Index(View):
    template_name = 'index.html'
