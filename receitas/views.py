from django.shortcuts import render, get_object_or_404
from .models import Receita

# Create your views here.

def home(request):
    categoria_slug = request.GET.get('categoria')

    categorias_choices = [choice[0] for choice in Receita.CATEGORIAS]

    if categoria_slug:
        receitas = Receita.objects.filter(categoria=categoria_slug)
        categorias_selecionada = categoria_slug
    else:
        receitas = Receita.objects.all()
        categorias_selecionada = None

    return render(request, 'receitas/home.html', {
        'receitas': receitas,
        'categorias': categorias_choices,
        'categoria_selecionada': categorias_selecionada,
    })

def receita_detail(request, id):
    receita = get_object_or_404(Receita, pk=id)
    return render(request, 'receitas/receita_detail.html', {'receita': receita})

def pesquisar_receitas(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = Receita.objects.filter(title__icontains=query)

    return render(request, 'receitas/pesquisa.html',{
        'query': query,
        'resultados': resultados
    })