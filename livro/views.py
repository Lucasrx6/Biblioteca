from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimos
from .forms import Cadastro_livro

# Create your views here.

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario)
        form = Cadastro_livro()
        return render(request, 'home.html', {'livros': livros,
                                             'usuario_logado': request.session.get('usuario'),
                                             'form': form})
    else:
        return redirect('/auth/login/?status=2')

def ver_livros(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id = id)
        if request.session.get('usuario') == livros.usuario.id:
            categoria_livro = Categoria.objects.filter(usuario_id = request.session.get('usuario'))
            emprestimos = Emprestimos.objects.filter(livro = livros)
            return render(request,'ver_livro.html', {'livro': livros,
                                                     'categoria_livro': categoria_livro,
                                                     'emprestimos':emprestimos,
                                                     'usuario_logado': request.session.get('usuario')})
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('auth/login/?status=2')

def cadastrar_livro(request):
    if request.method == 'POST':
        form = Cadastro_livro(request.POST)

        if form.is_valid():
            form.save()
        else:
            return HttpResponse('Dados Invalidos')
