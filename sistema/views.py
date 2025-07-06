from django.shortcuts import render, redirect
from .forms import LocacaoForm
from django.contrib import messages
from .models import Locacao
from django.db.models import Sum, Count, Q



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
    locacoes = Locacao.objects.select_related(
        'cliente').prefetch_related('brinquedos').order_by('-data_inicio')

    nome_cliente = request.GET.get('cliente')
    data = request.GET.get('data')

    if nome_cliente:
        locacoes = locacoes.filter(cliente__nome__icontains=nome_cliente)

    if data:
        locacoes = locacoes.filter(data_inicio=data)

    return render(request, 'sistema/listar_locacoes.html', {
        'locacoes': locacoes,
        'nome_cliente': nome_cliente or '',
        'data_filtro': data or '',
    })


def dashboard_financeiro(request):
    data_inicio = request.GET.get('inicio')
    data_fim = request.GET.get('fim')
    status = request.GET.get('status')
    
    locacoes = Locacao.objects.all()
    
    if data_inicio:
        locacoes = locacoes.filter(data_inicio__gte=data_inicio)
    if data_fim:
        locacoes = locacoes.filter(data_fim__lte=data_fim)
    if status:
        locacoes = locacoes.filter(status_pagamento=status)
      
    total_recebido = locacoes.filter(status_pagamento='pago').aggregate(
        Sum('valor_total'))['valor_total__sum'] or 0
    total_pendente = locacoes.filter(status_pagamento='pendente').aggregate(
        Sum('valor_total'))['valor_total__sum'] or 0
    total_cancelado = locacoes.filter(status_pagamento='cancelado').aggregate(
        Sum('valor_total'))['valor_total__sum'] or 0
    total_geral = locacoes.aggregate(Sum('valor_total'))[
        'valor_total__sum'] or 0

    return render(request, 'sistema/dashboard_financeiro.html', {
        'locacoes': locacoes,
        'total_recebido': total_recebido,
        'total_pendente': total_pendente,
        'total_cancelado': total_cancelado,
        'total_geral': total_geral,
        'filtro_inicio': data_inicio or '',
        'filtro_fim': data_fim or '',
        'filtro_status': status or '',
    })