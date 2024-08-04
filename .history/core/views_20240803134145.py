from django.shortcuts import render
from django.views.generic import View,TemplateView
from .models import *
from django.db.models import Sum

'''class Index(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        vendas =  VendaDoProduto.objects.all()
        total = sum(vendas.total for item in vendas)


        return render(request, self.template_name, {'vendas':vendas, 'total':total})
    '''
class Index(TemplateView):
    template_name = 'index2.html'
    def get(self, request):
        vendas = VendaDoProduto.objects.all()
        # Calcula a soma de todos os valores do campo 'total' de cada instância de 'VendaDoProduto' em 'vendas'.
        # A verificação 'if item.total' garante que apenas valores não nulos sejam incluídos na soma.

        total = sum(item.total for item in vendas if item.total)
        # Calcula a quantidade total vendida de cada produto e o total em vendas
        produtos_vendidos = VendaDoProduto.objects.values('produto__nome_produto').annotate(
            total_vendido=Sum('qtd'), total_revenue=Sum('total')
        ).order_by('-total_vendido')
        
        # Obtém o produto mais vendido
        mais_vendido = produtos_vendidos.first() if produtos_vendidos else None


        
        return render(request, self.template_name, {'vendas': vendas, 'total': total, 'mais_vendido':mais_vendido})  