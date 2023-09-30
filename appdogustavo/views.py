from django.shortcuts import render, redirect
from .models import Motivos, Pokemons, TabelaData

from .forms import CreateFormP, CreateFormM




# Create your views here.
def home(request):

  motivos = Motivos.objects.all()
  pokemons = Pokemons.objects.all()
  data = TabelaData.objects.all()
  return render(request, "home.html", {"motivos":motivos, "pokemons":pokemons, "tabeladata":data})

def create_motivo(request):
  if 'voltar' in request.POST:
    return redirect(home)
  if request.method=='POST':
    formM = CreateFormM(request.POST)
    if formM.is_valid():
      formM.save()
    return redirect(home)
    
  return render(request, "forms.html", context={'action' : 'Adicionar', 'tipo' : 'Motivos', 'formM' : CreateFormM})

def update_motivo(request, id):
  motivo = Motivos.objects.get(id = id)
  formM = CreateFormM(instance=motivo)
  if 'voltar' in request.POST:
    return redirect(home)
  if request.method=='POST':
    formM = CreateFormM(request.POST, instance=motivo)
    if formM.is_valid():
      formM.save()
    return redirect(home)
  
  return render(request, "forms.html", context={'action' : 'Atualizar', 'tipo' : 'Motivos', 'formM' : formM, "motivo": motivo})

def delete_motivo(request, id):
  motivo = Motivos.objects.get(id = id)
  if request.method=='POST':
    if 'confirm' in request.POST:
      motivo.delete()
    return redirect(home)
  return render(request, "are_you_sure.html", context={'tipo' : 'motivo', "nome": motivo.title})

def create_pokemon(request):
  if 'voltar' in request.POST:
    return redirect(home)
  if request.method=='POST':
    formP = CreateFormP(request.POST)
    if formP.is_valid():
      formP.save()
    return redirect(home)

  return render(request, "forms.html", context={'action' : 'Adicionar', 'tipo' : 'Pokémons', 'formP' : CreateFormP})

def update_pokemon(request, id):
  pokemon = Pokemons.objects.get(id = id)
  formP = CreateFormP(instance=pokemon)
  if 'voltar' in request.POST:
    return redirect(home)
  if request.method=='POST':
    formP = CreateFormP(request.POST, instance=pokemon)
    if formP.is_valid():
      formP.save()
    return redirect(home)

  return render(request, "forms.html", context={'action' : 'Atualizar', 'tipo' : 'Pokémons', 'formP' : formP, 'pokemon': pokemon})

def delete_pokemon(request, id):
  pokemon = Pokemons.objects.get(id = id)
  if request.method=='POST':
    if 'confirm' in request.POST:
      pokemon.delete()
    return redirect(home)
  return render(request, "are_you_sure.html", context={'tipo' : 'Pokémon', "nome": pokemon.title})