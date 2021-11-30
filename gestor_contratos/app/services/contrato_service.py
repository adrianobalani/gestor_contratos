from ..models import Contrato

def cadastrar_contrato(contrato):
    Contrato.objects.create(razaosocial=contrato.razaosocial, cnpj=contrato.cnpj, inscricao=contrato.inscricao, nome=contrato.nome, 
                            produto=contrato.produto, endereco=contrato.endereco, bairro=contrato.bairro, cidade=contrato.cidade, 
                            uf=contrato.uf, cep=contrato.cep, telefone=contrato.telefone, email=contrato.email,
                            insercoes=contrato.insercoes, tipo_insercao=contrato.tipo_insercao, pagamento=contrato.pagamento,
                            valor_total=contrato.valor_total, parcelas=contrato.parcelas, valor_parcelas=contrato.valor_parcelas, 
                            vencimento=contrato.vencimento, observacoes=contrato.observacoes, usuario=contrato.usuario)
def listar_contratos(usuario):
    return Contrato.objects.filter(usuario=usuario).all()

def listar_contrato_id(id):
    return Contrato.objects.get(id=id)

def editar_contrato(contrato_bd, contrato_novo):
    contrato_bd.razaosocial = contrato_novo.razaosocial
    contrato_bd.cnpj = contrato_novo.cnpj
    contrato_bd.inscricao = contrato_novo.inscricao
    contrato_bd.nome = contrato_novo.nome
    contrato_bd.produto = contrato_novo.produto
    contrato_bd.endereco = contrato_novo.endereco
    contrato_bd.bairro = contrato_novo.bairro
    contrato_bd.cidade = contrato_novo.cidade
    contrato_bd.uf = contrato_novo.uf
    contrato_bd.cep = contrato_novo.cep
    contrato_bd.telefone = contrato_novo.telefone
    contrato_bd.email = contrato_novo.email
    contrato_bd.insercoes = contrato_novo.insercoes
    contrato_bd.tipo_insercao = contrato_novo.tipo_insercoes
    contrato_bd.pagamento = contrato_novo.pagamento
    contrato_bd.valor_total = contrato_novo.valor_total
    contrato_bd.parcelas = contrato_novo.parcelas
    contrato_bd.valor_parcelas = contrato_novo.valor_parcelas
    contrato_bd.vencimento = contrato_novo.vencimento
    contrato_bd.observacoes = contrato_novo.observacoes            
    contrato_bd.save(force_update=True)

def remover_contrato(contrato_bd):
    contrato_bd.delete()