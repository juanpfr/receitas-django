from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('receitas/<int:id>/', views.receita_detail, name='receita_detail'),
    path('pesquisar/', views.pesquisar_receitas, name='pesquisar_receitas'),
]