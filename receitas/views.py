from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Receita

# Create your views here.

def home(request):
    return render(request, 'receitas/home.html')

def receita_detail(request, id):
    receita = get_object_or_404(Receita, pk=id)

    context = {
        'receita': receita,
    }

    return render(request, 'receitas/receita_detail.html', context)
    