import livros
from django.core.checks import messages
from django.shortcuts import redirect, render
from livros.models import Livro
from livros.forms import *

def index(request):
    livros = Livro.objects.all()
    return render(request, 'home.html', {'livros':livros})

def detalhes(request, livro_id):
    livro = Livro.objects.get(pk=livro_id)
    return render(request, 'detalhes.html', {'livro':livro})

def cadastrar(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(index)
        return render(request, 'cadastrar.html', {'form':form}) 

    form = LivroForm()
    return render(request, 'cadastrar.html', {'form':form})

def editar(request, livro_id):
    livro = Livro.objects.get(pk=livro_id)
    form = LivroForm(request.POST or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect(index)
    return render(request, 'editar.html', {'form':form})

def excluir(request, livro_id):
    livro = Livro.objects.get(pk=livro_id)
    livro.delete()

    return redirect(index)