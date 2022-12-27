from django.db import models
from clientes.models import Cliente
from .choices import ChoicesCategoriaManutencao


class CategoriaManutencao(models.Model):
    titulo = models.CharField(max_length=3, choices=ChoicesCategoriaManutencao.choices)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.titulo


class Servico(models.Model):
    titulo = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    CategoriaManutencao = models.ManyToManyField(CategoriaManutencao)
    
    data_inicio = models.DateField(null=True)
    data_entrega = models.DateField(null=True)
    finalizado = models.BooleanField(default=False)
    protocolo = models.CharField(max_length=32, null=True, blank=True)
    
