from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimos
from .forms import Cadastro_livro, Cadastro_categoria


# Create your views here.

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario)
        status_categoria = request.GET.get('cadastro_categoria')
        status_livro = request.GET.get('cadastro_livro')
        form = Cadastro_livro()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
        form_categoria = Cadastro_categoria()

        return render(request, 'home.html', {'livros': livros,
                                             'usuario_logado': request.session.get('usuario'),
                                             'form': form,
                                             'id_livro': id,
                                             'form_categoria': form_categoria,
                                             'status_categoria': status_categoria,
                                             'status_livro': status_livro})
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
                                                     'usuario_logado': request.session.get('usuario'),
                                                     'id_livro': id})
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('auth/login/?status=2')

def cadastrar_livro(request):
    if request.method == 'POST':
        form = Cadastro_livro(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/livro/home/?cadastro_livro=1')
        else:
            return HttpResponse('Dados Invalidos')

def excluir_livro(request, id):
    livro = Livros.objects.get(id = id).delete()
    return redirect('/livro/home')

def cadastrar_categoria(request):
    if request.method == 'POST':
        form = Cadastro_categoria(request.POST)
        nome = form.data['nome']
        descricao = form.data['descricao']
        id_usuario = request.POST.get('usuario')
        if int(id_usuario) == int(request.session.get('usuario')):
            user = Usuario.objects.get(id = id_usuario)
            categoria = Categoria(nome=nome, descricao=descricao, usuario=user)
            categoria.save()
            return redirect('/livro/home/?cadastro_categoria=1')
        else:
            return HttpResponse('Erro')