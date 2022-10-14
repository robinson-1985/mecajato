from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Cliente, Carro
import re

def clientes(request):
    if request.method == 'GET':
        clientes_list = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes_list': clientes_list})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.get('carro')
        placas = request.POST.get('placa')
        anos = request.POST.get('ano')

        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email,
             'carros': zip(carros, placas, anos) })
        
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), 
        email):
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 
            'carros': zip(carros, placas, anos)})

        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )

        cliente.save()

        for carro, placa, ano in zip(carros, placas, anos):
            car = Carro(carro=carro, placa=placa, ano=ano, cliente=cliente)
            car.save()

        return HttpResponse('teste')


def att_cliente(request):
    return JsonResponse({'teste': 1})