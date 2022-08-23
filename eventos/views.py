from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from eventos.models import Evento

@csrf_exempt
def index(request):
  
    return render(request, template_name='index.html', context={'eventos': Evento.objects.all()})

@csrf_exempt
def add_evento (request):
    nome = request.POST.get('nome_evento')
    evento = Evento.objects.create(nome=nome)
    
    return render(request, template_name='fragmentos/lista_eventos.html', context={'eventos': Evento.objects.all()})

@csrf_exempt
def remove_evento (request, pk):
    Evento.objects.filter(pk=pk).delete()
    
    return render(request, template_name='fragmentos/lista_eventos.html', context={'eventos': Evento.objects.all()})

@csrf_exempt
def search_evento (request):
    nome = request.POST.get('nome_busca')
    if nome != "":
        resultados = Evento.objects.filter(nome__istartswith=nome)
    
        if resultados.exists():
            return render(request, template_name='fragmentos/lista_busca.html', context={'eventos_busca': resultados})

        else:
            return HttpResponse("<span style='color:red;'>não há eventos!</span>")
    else:
        return HttpResponse("<span style='color:gray;'>digite!</span>")    
        

    
