from django.forms import ModelForm
from django import forms
from .models import Pokemons, Motivos

class CreateFormP(ModelForm):
  name = forms.TextInput()
  
  class Meta:
    model = Pokemons
    fields = '__all__'

# class UpdateFormP(ModelForm):
#   name = forms.TextInput()

#   class Meta:
#     model = Pokemons
#     fields = '__all__'
    
class CreateFormM(ModelForm):
  name = forms.TextInput()

  class Meta:
    model = Motivos
    fields = '__all__'

# class UpdateFormM(ModelForm):
#   name = forms.TextInput()

#   class Meta:
#     model = Motivos
#     fields = '__all__'