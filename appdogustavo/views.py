from django.shortcuts import render, redirect
from .models import Motivos, Pokemons, TabelaData
from .forms import CreateFormP, CreateFormM
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):

  motivos = Motivos.objects.all()
  pokemons = Pokemons.objects.all()
  data = TabelaData.objects.all()
  return render(request, "home.html", {"motivos":motivos, "pokemons":pokemons, "tabeladata":data})

@login_required
def create_motivo(request):
  if 'voltar' in request.POST:
    return redirect("home")
  if request.method=='POST':
    formM = CreateFormM(request.POST)
    if formM.is_valid():
      formM.save()
    return redirect("home")
    
  return render(request, "forms.html", context={'action' : 'Adicionar', 'tipo' : 'Motivos', 'formM' : CreateFormM})

@login_required
def update_motivo(request, id):
  motivo = Motivos.objects.get(id = id)
  formM = CreateFormM(instance=motivo)
  if 'voltar' in request.POST:
    return redirect("home")
  if request.method=='POST':
    formM = CreateFormM(request.POST, instance=motivo)
    if formM.is_valid():
      formM.save()
    return redirect("home")
  
  return render(request, "forms.html", context={'action' : 'Atualizar', 'tipo' : 'Motivos', 'formM' : formM, "motivo": motivo})

@login_required
def delete_motivo(request, id):
  motivo = Motivos.objects.get(id = id)
  if request.method=='POST':
    if 'confirm' in request.POST:
      motivo.delete()
    return redirect("home")
  return render(request, "are_you_sure.html", context={'tipo' : 'motivo', "nome": motivo.title})

@login_required
def create_pokemon(request):
  if 'voltar' in request.POST:
    return redirect("home")
  if request.method=='POST':
    formP = CreateFormP(request.POST)
    if formP.is_valid():
      formP.save()
    return redirect("home")

  return render(request, "forms.html", context={'action' : 'Adicionar', 'tipo' : 'Pokémons', 'formP' : CreateFormP})

@login_required
def update_pokemon(request, id):
  pokemon = Pokemons.objects.get(id = id)
  formP = CreateFormP(instance=pokemon)
  if 'voltar' in request.POST:
    return redirect("home")
  if request.method=='POST':
    formP = CreateFormP(request.POST, instance=pokemon)
    if formP.is_valid():
      formP.save()
    return redirect("home")

  return render(request, "forms.html", context={'action' : 'Atualizar', 'tipo' : 'Pokémons', 'formP' : formP, 'pokemon': pokemon})

@login_required
def delete_pokemon(request, id):
  pokemon = Pokemons.objects.get(id = id)
  if request.method=='POST':
    if 'confirm' in request.POST:
      pokemon.delete()
    return redirect("home")
  return render(request, "are_you_sure.html", context={'tipo' : 'Pokémon', "nome": pokemon.title})

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
    user.save()
    return redirect("home")
  return render(request, "register.html", context={"action": "Adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(username = request.POST["username"], password = request.POST["password"])

    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
  
    if request.user.is_authenticated:
      return redirect("home")
    return render(request, "login.html", context={"error_msg": "Usuário não pôde ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")