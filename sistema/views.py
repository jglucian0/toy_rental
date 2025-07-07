from django.shortcuts import render, redirect, get_object_or_404
from .forms import LocacaoForm, ClienteForm
from django.contrib import messages
from .models import Brinquedo, Locacao
import urllib.parse
from django.db.models import Sum, Count, Q
from unidecode import unidecode


def enviar_confirmacao_whatsapp(request, locacao_id):
    locacao = get_object_or_404(Locacao, pk=locacao_id)
    cliente = locacao.cliente

    brinquedos = ', '.join(
        [brinquedo.nome for brinquedo in locacao.brinquedos.all()])


    mensagem = (
    f"Olá {cliente.nome}!\n\n"
    f"Sua locação foi confirmada:\n"
    f"📅 Período: {locacao.data_inicio.strftime('%d/%m/%Y')} a {locacao.data_fim.strftime('%d/%m/%Y')}\n"
    f"🎠 Brinquedos: {brinquedos}\n"
    f"💰 Valor total: R$ {locacao.valor_total}\n"
    f"📌 Status: {locacao.get_status_pagamento_display()}\n\n"
    f"Agradecemos por escolher a Happy Kids!")

    mensagem_encoded = urllib.parse.quote_plus(mensagem)

    numero = cliente.telefone.replace(" ", "").replace(
        "(", "").replace(")", "").replace("-", "")
    if not numero.startswith("55"):
        numero = "55" + numero  # adiciona código do Brasil se necessário

    url = f"https://wa.me/{numero}?text={mensagem_encoded}"
    return redirect(url)


def excluir_locacao(request, locacao_id):
    locacao = get_object_or_404(Locacao, pk=locacao_id)

    if request.method == 'POST':
        locacao.delete()
        messages.success(request, 'Locação excluída com sucesso.')
        return redirect('listar_locacoes')

    return render(request, 'sistema/confirmar_exclusao.html', {'locacao': locacao})


def editar_status_pagamento(request, locacao_id):
    locacao = get_object_or_404(Locacao, pk=locacao_id)

    if request.method == 'POST':
        novo_status = request.POST.get('status_pagamento')
        if novo_status in dict(Locacao.STATUS_PAGAMENTO).keys():
            locacao.status_pagamento = novo_status
            locacao.save()
            messages.success(request, "Status de pagamento atualizado com sucesso!")
            return redirect('listar_locacoes')
        
    return render(request, 'sistema/editar_status_pagamento.html', {
        'locacao': locacao,
        'opcoes_status': Locacao.STATUS_PAGAMENTO,
    })
    
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_locacoes')
    else:
        form = ClienteForm()
    return render(request, 'sistema/cadastrar_cliente.html', {'form': form})

def agendar_locacao(request):
    form = LocacaoForm()
    brinquedos = Brinquedo.objects.all()
    return render(request, 'sistema/agendar_locacao.html', {
        'form': form,
        'brinquedos': brinquedos,
    })
    
    return render(request, 'sistema/agendar_locacao.html', {'form': form, 'brinquedos': brinquedos})


def listar_locacoes(request):
    locacoes = Locacao.objects.select_related(
        'cliente').prefetch_related('brinquedos').order_by('-data_inicio')

    nome_cliente = request.GET.get('cliente')
    data = request.GET.get('data')

    if nome_cliente:
        locacoes = [l for l in locacoes if unidecode(
            nome_cliente.lower()) in unidecode(l.cliente.nome.lower())]

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