from django.shortcuts import render
from .forms import PedidoForm

def home(req):
    # nome = 'Anna'
    # lista_nomes = ['a', 'b', 'c']
    # args = {
    #     'nome' : nome,
    #     'lista': lista_nomes,
    # }
    return render(req, 'home.html')

def post(req):
    return render(req, 'posts.html')

def cadastro(req):
    form = PedidoForm(req.POST or None)
    if form.is_valid():
        form.save()
        context = {
            'msg': 'O pedido deu certo!'
        }
        return render(req, 'cadastro.html', context)
    context = {
        'formulario': form
    }
    return render(req, 'cadastro.html', context)
