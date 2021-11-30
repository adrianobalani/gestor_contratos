from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import ContratoForm
from ..operations.tasks import Contrato
from ..services import contrato_service

# Create your views here.

@login_required()
def listar_contratos(request):
    contratos = contrato_service.listar_contratos(request.user)
    return render(request, 'contratos/listar_contratos.html', {"contratos": contratos})

@login_required()
def cadastrar_contrato(request):
    if request.method == "POST":
        form_contrato = ContratoForm(request.POST)

        if form_contrato.is_valid():
            razaosocial = form_contrato.cleaned_data["razaosocial"]
            cnpj = form_contrato.cleaned_data["cnpj"]
            inscricao = form_contrato.cleaned_data["inscricao"]
            nome = form_contrato.cleaned_data["nome"]
            produto = form_contrato.cleaned_data["produto"]
            endereco = form_contrato.cleaned_data["endereco"]
            bairro = form_contrato.cleaned_data["bairro"]
            cidade = form_contrato.cleaned_data["cidade"]
            uf = form_contrato.cleaned_data["uf"]
            cep = form_contrato.cleaned_data["cep"]
            telefone = form_contrato.cleaned_data["telefone"]
            email = form_contrato.cleaned_data["email"]
            insercoes = form_contrato.cleaned_data["insercoes"]
            tipo_insercao = form_contrato.cleaned_data["tipo_insercao"]
            pagamento = form_contrato.cleaned_data["pagamento"]
            valor_total = form_contrato.cleaned_data["valor_total"]
            parcelas = form_contrato.cleaned_data["parcelas"]
            valor_parcelas = form_contrato.cleaned_data["valor_parcelas"]
            vencimento = form_contrato.cleaned_data["vencimento"]
            observacoes = form_contrato.cleaned_data["observacoes"]

            contrato_novo = Contrato(razaosocial=razaosocial, cnpj=cnpj, inscricao=inscricao, nome=nome, 
                                     produto=produto, endereco=endereco, bairro=bairro, cidade=cidade, 
                                     uf=uf, cep=cep, telefone=telefone,  email=email, insercoes=insercoes, 
                                     tipo_insercao=tipo_insercao, pagamento=pagamento, valor_total=valor_total, 
                                     parcelas=parcelas, valor_parcelas=valor_parcelas, vencimento=vencimento, 
                                     observacoes=observacoes, usuario=request.user)
            
            contrato_service.cadastrar_contrato(contrato_novo)
            return redirect('listar_contratos')
    else:
        form_contrato = ContratoForm()
    return render(request, 'contratos/form_contrato2.html', {'form_contrato': form_contrato})

@login_required()
def editar_contrato(request, id):
    contrato_bd = contrato_service.listar_contrato_id(id)
    if contrato_bd.usuario != request.user:
        return HttpResponse("Não permitido")
    form_contrato = ContratoForm(request.POST or None, instance=contrato_bd)
    if form_contrato.is_valid():
        razaosocial = form_contrato.cleaned_data["razaosocial"]
        cnpj = form_contrato.cleaned_data["cnpj"]
        inscricao = form_contrato.cleaned_data["inscricao"]
        nome = form_contrato.cleaned_data["nome"]
        produto = form_contrato.cleaned_data["produto"]
        endereco = form_contrato.cleaned_data["endereco"]
        bairro = form_contrato.cleaned_data["bairro"]
        cidade = form_contrato.cleaned_data["cidade"]
        uf = form_contrato.cleaned_data["uf"]
        cep = form_contrato.cleaned_data["cep"]
        telefone = form_contrato.cleaned_data["telefone"]
        email = form_contrato.cleaned_data["email"]
        insercoes = form_contrato.cleaned_data["insercoes"]
        tipo_insercao = form_contrato.cleaned_data["tipo_insercao"]
        pagamento = form_contrato.cleaned_data["pagamento"]
        valor_total = form_contrato.cleaned_data["valor_total"]
        parcelas = form_contrato.cleaned_data["parcelas"]
        valor_parcelas = form_contrato.cleaned_data["valor_parcelas"]
        vencimento = form_contrato.cleaned_data["vencimento"]
        observacoes = form_contrato.cleaned_data["observacoes"]

        contrato_novo = Contrato(razaosocial=razaosocial, cnpj=cnpj, inscricao=inscricao, nome=nome, 
                                     produto=produto, endereco=endereco, bairro=bairro, cidade=cidade, 
                                     uf=uf, cep=cep, telefone=telefone,  email=email, insercoes=insercoes, 
                                     tipo_insercao=tipo_insercao, pagamento=pagamento, valor_total=valor_total, 
                                     parcelas=parcelas, valor_parcelas=valor_parcelas, vencimento=vencimento, 
                                     observacoes=observacoes, usuario=request.user)
        
        contrato_service.editar_contrato(contrato_bd, contrato_novo)
        return redirect('listar_contratos')
    return render(request, 'contratos/form_contrato.html', {"form_contrato": form_contrato})

@login_required()
def remover_contrato(request, id):
    contrato_bd = contrato_service.listar_contrato_id(id)
    if contrato_bd.usuario != request.user:
        return HttpResponse("Não permitido")
    if request.method == "POST":
        contrato_service.remover_contrato(contrato_bd)
        return redirect('listar_contrato')
    return render(request, 'contratos/confirma_exclusao.html', {'contrato': contrato_bd})
