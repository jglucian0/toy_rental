from django.shortcuts import render, redirect
from .forms import LocacaoForm
from django.contrib import messages
from .models import Locacao

def agendar_locacao(request):
    if request.method == 'POST':
        form = LocacaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Locação agendada com sucesso!")
            return redirect('agendar_locacao')
    else:
        form = LocacaoForm()
    
    return render(request, 'sistema/agendar_locacao.html', {'form': form})
  

def listar_locacoes(request):
    locacoes = Locacao.objects.select_related('cliente').prefetch_related('brinquedos').order_by('-data_inicio')
    return render(request, 'sistema/listar_locacoes.html', {'locacoes': locacoes})
