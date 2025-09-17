from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import Receita
from .forms import ContatoForm

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

def sobre_nos(request):
    return render(request, 'receitas/sobre_nos.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            send_mail(
                f'Mensagem de {nome}',
                f'Mensagem de {nome} ({email}):\n\n{mensagem}',
                email,
                ['seu_email_para_receber@exemplo.com'],
                fail_silently=False,
            )

            return redirect(reverse('sucesso'))
        
    else:
        form = ContatoForm()

    return render(request, 'receitas/contato.html', {'form': form})

def sucesso(request):
    return render(request, 'receitas/sucesso.html')

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