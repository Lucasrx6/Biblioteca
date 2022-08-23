from django import forms
from .models import Livros, Categoria
from django.db.models import fields
from django.db import models
from datetime import date


class Cadastro_livro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ('__all__')

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()

class Cadastro_categoria(forms.Form):
    nome = forms.CharField(max_length=30)
    descricao = forms.CharField(max_length=60)

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descricao'].widget = forms.Textarea()