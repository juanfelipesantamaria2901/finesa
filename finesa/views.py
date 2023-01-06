from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def polizavida(request):
    return render(request, 'TablaPólizaVida.html')

def polizahogar(request):
    return render(request, 'TablaPólizaHogar.html')

def polizaauto(request):
    return render(request, 'TablaPólizaAuto.html')

def formulario_emision1(request):
    return render(request, 'FormularioEmision1.html')

def formulario_emision3(request):
    return render(request, 'FomularioEmision3.html')

def formulario_emision4(request):
    return render(request, 'FormularioEmsion4.html')

def formulario_inspecion(request):
    return render(request, 'FormularioInspeción.html')

def formulario(request):
    return render(request, 'Formulario.html')

