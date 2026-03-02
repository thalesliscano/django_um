from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect, get_object_or_404
from core.models import Produto

from django.http import HttpResponse
from django.template import loader
def index(request):
    produtos = Produto.objects.all()

    print(dir(request))

    # só pra testa alguns métodos contidos na request

    # print("is_authenticated:", request.user.is_authenticated)
    # print(f"User {request.user.is_anonymous}")
    # print("user_id:", request.user.id)
    # # print(f"User {dir(request.user)}")

    if(request.user.is_anonymous):
        logado = "Usuário não logado"
    else:
        logado = "Usuário logado"


    context = {
        "curso":"Programação Web com Django Framework",
        "outro": "descrição bla bla bla bla bla",
        "logado": logado,
        "produtos": produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    # prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto,id=id)
    context = {
        'produto':prod
    }
    print(f"id: {id}")
    return render(request, 'produto.html', context)

def sair(request):
    logout(request)
    return redirect('/')
    pass

def error404(request,exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
