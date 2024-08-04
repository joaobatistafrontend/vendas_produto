from django.shortcuts import render
from django.views.generic import View,TemplateView
from .models import *

class Index(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        vendas =  VendaDoProduto.objects.all()
        itens = ItemDoCarrinho.objects.filter(empresa=empresa)
        total = sum(vendas.total for item in itens)


        return render(request, self.template_name, {'vendas':vendas})