from django.db import models

# Create your models here.
class Motivos(models.Model):
  EXPRESSIVIDADE = [
    ("G", "Grande"),
    ("M", "Média"),
    ("P", "Pequena"),
  ]
  
  CATEGORY = [
    ("B", "Bonito"),
    ("E", "Engraçado"),
    ("C", "Competitivo"),
  ]
  title = models.CharField(max_length=70)
  relevancia = models.CharField(max_length=70)
  ExpressividadeInGame = models.CharField(max_length=1, choices=EXPRESSIVIDADE)
  categoria = models.CharField(max_length=1, choices=CATEGORY)

class Pokemons(models.Model):
  title = models.CharField(max_length=70)
  tipo = models.CharField(max_length=20)
  tamanho = models.CharField(max_length=20)
  peso = models.CharField(max_length=20)
  img = models.CharField(max_length=200, blank=True, null=True)
  color = models.CharField(max_length=200, blank=True, null=True)

class TabelaData(models.Model):
  title = models.CharField(max_length=50)
  statS = models.IntegerField()
  statM = models.IntegerField()