import livros
from django.shortcuts import render
from livros.models import Livro

def index(request):
    livros = Livro.objects.all()
    return render(request, 'home.html', {'livros':livros})

def detalhes(request, livro_id):
    livro = Livro.objects.get(pk=livro_id)
    return render(request, 'detalhes.html', {'livro':livro})