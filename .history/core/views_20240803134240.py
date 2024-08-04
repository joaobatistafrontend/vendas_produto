from django.shortcuts import render
from django.views.generic import View,TemplateView
from .models import *
from django.db.models import Sum
from django.db.models import Sum
from datetime import datetime, timedelta
'''class Index(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        vendas =  VendaDoProduto.objects.all()
        total = sum(vendas.total for item in vendas)


        return render(request, self.template_name, {'vendas':vendas, 'total':total})
    '''
class Index(TemplateView):
    template_name = 'index3.html'
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

        # Obtém a data atual
        hoje = datetime.now().date()
        
        # Filtra as vendas do dia
        vendas_dia = VendaDoProduto.objects.filter(data_venda=hoje)
        total_dia = sum(item.total for item in vendas_dia if item.total)
        
        # Filtra as vendas da semana
        inicio_semana = hoje - timedelta(days=hoje.weekday())
        vendas_semana = VendaDoProduto.objects.filter(data_venda__gte=inicio_semana, data_venda__lte=hoje)
        total_semana = sum(item.total for item in vendas_semana if item.total)
        
        # Filtra as vendas do mês
        inicio_mes = hoje.replace(day=1)
        vendas_mes = VendaDoProduto.objects.filter(data_venda__gte=inicio_mes, data_venda__lte=hoje)
        total_mes = sum(item.total for item in vendas_mes if item.total)
        

        return render(request, self.template_name, {
                    'vendas': vendas,
                    'total': total,
                    'mais_vendido': mais_vendido,
                    'total_dia': total_dia,
                    'total_semana': total_semana,
                    'total_mes': total_mes
                })