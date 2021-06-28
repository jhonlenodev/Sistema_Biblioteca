from django import forms
from django.db.models import fields
from livros.models import *

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'