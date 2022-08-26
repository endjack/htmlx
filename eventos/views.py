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
    
    response = render(request, template_name='fragmentos/lista_eventos.html', context={'eventos': Evento.objects.all()})
    response['HX-Trigger'] = 'eventoAdd'
    return response

@csrf_exempt
def remove_evento (request, pk):
    Evento.objects.filter(pk=pk).delete()
    
    response = render(request, template_name='fragmentos/lista_eventos.html', context={'eventos': Evento.objects.all()})
    response['HX-Trigger'] = 'eventoRemove'
    return response

@csrf_exempt
def detalhar_evento (request, pk): 
    context = {
            'evento': Evento.objects.get(pk=pk),
            'include': request.POST.get("evento_input")
    }
    return render(request, template_name='fragmentos/detalhar-evento.html', context=context)

@csrf_exempt
def editar_evento(request, pk): 
    context = {
            'evento': Evento.objects.get(pk=pk),
    }
    return render(request, template_name='fragmentos/editar-evento.html', context=context)

@csrf_exempt
def get_evento(request): 
    
    return HttpResponse("<span class='mensagem' style='color:red'>Trigger chamado ao adicionar Evento</span>")

@csrf_exempt
def atualizar_evento(request, pk): 
    
    novo_nome = request.POST.get("nome")
    evento = Evento.objects.filter(pk=pk).update(nome=novo_nome)

    context = {
            'evento': Evento.objects.get(pk=pk),
    }
    return render(request, template_name='fragmentos/detalhar-evento.html', context=context)

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
        

    
