from django.shortcuts import render
from django.views.generic import View,TemplateView
from .models import *

class Index(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        v
        return render(request, self.template_name)