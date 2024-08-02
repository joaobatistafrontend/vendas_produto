from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import date



class NovaCategoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.nome}'

class NovoValor(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'R${self.valor}'
    

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100, blank=True, null=True)  # Nome do produto
    tipo_categoria = models.ForeignKey(NovaCategoria, on_delete=models.CASCADE)  # Categoria do produto
    valor = models.ForeignKey(NovoValor, on_delete=models.CASCADE)  # Valor do produto

    def __str__(self):
        return f"{self.nome_produto} - {self.tipo_categoria.nome} - R${self.valor.valor}"

class VendaDoProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  # Produto vendido
    qtd = models.IntegerField(blank=True, null=True)  # Quantidade vendida
    data_venda = models.DateField()  # Data da venda, definida automaticamente para a data atual
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Total calculado

    def __str__(self):
        return f"{self.produto.nome_produto} - {self.qtd} unidades - Total: R${self.total} - data {self.data_venda}"

# Função que será chamada antes de salvar uma instância de VendaDoProduto
@receiver(pre_save, sender=VendaDoProduto)
def update_total(sender, instance, **kwargs):
    # Verifica se o produto e a quantidade não são nulos e calcula o total
    if instance.produto.valor and instance.qtd:
        instance.total = instance.produto.valor.valor * instance.qtd
    else:
        instance.total = 0  # Define total como 0 se valor ou qtd forem nulos