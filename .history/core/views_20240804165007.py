from django.shortcuts import render
from django.views.generic import View,TemplateView
from .models import *
from django.db.models import Sum
from django.db.models import Sum
from datetime import datetime, timedelta


def infor()

class IndexMes(TemplateView):
    template_name = 'dashboard.html'
    
    def get(self, request):
        vendas = VendaDoProduto.objects.all()
        
        # Calcula a soma total de todas as vendas
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

        # Agrupa as vendas por mês
        vendas_mensais = VendaDoProduto.objects.values('data_venda__year', 'data_venda__month').annotate(
            total_mensal=Sum('total')
        ).order_by('data_venda__year', 'data_venda__month')

        # Determina o primeiro mês com vendas
        if vendas_mensais:
            primeiro_ano = vendas_mensais[0]['data_venda__year']
            primeiro_mes = vendas_mensais[0]['data_venda__month']
        else:
            primeiro_ano = None
            primeiro_mes = None
        
        return render(request, self.template_name, {
            'vendas': vendas,
            'total': total,
            'mais_vendido': mais_vendido,
            'total_dia': total_dia,
            'total_semana': total_semana,
            'total_mes': total_mes,
            'vendas_mensais': vendas_mensais,
            'primeiro_ano': primeiro_ano,
            'primeiro_mes': primeiro_mes,
        })


class DetalhesDias(TemplateView):
    template_name = 'detalhesDias.html'
    def get(self, request):

        # Obtém a data atual
        hoje = datetime.now().date()
        
        # Filtra as vendas do dia
        vendas_dia = VendaDoProduto.objects.filter(data_venda=hoje)
        total_dia = sum(item.total for item in vendas_dia if item.total)

        return render(request, self.template_name, {'vendas_dia':vendas_dia, 'total_dia':total_dia})






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