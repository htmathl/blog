from django.shortcuts import render

# Create your views here.

def home(request):
    nome = 'Anna'
    lista_nomes = ['a', 'b', 'c']
    args = {
        'nome' : nome,
        'lista': lista_nomes,
    }
    return render(request, 'home.html', args)
