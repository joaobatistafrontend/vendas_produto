from django.shortcuts import render
from django.views.generic import View,TemplateView


class Index(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.tem)