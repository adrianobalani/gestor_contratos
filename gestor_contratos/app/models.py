from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contrato(models.Model):
    TIPO_PAGAMENTO = [
        ("avista", "Avista"),
        ("parcelado", "Parcelado"),
        ("cartao", "Cartão de Crédito"),
    ]

    TIPO_TEXTO = [
        ("Testemunhal", "Testemunhal"),
        ("Texto Gravado", "Texto Gravado"),
        ("Pedagio", "Pedágio"),
    ]
    
  
    razaosocial = models.CharField('Razão Social', max_length = 100, blank=False, null=False)
    cnpj = models.CharField('CNPJ', max_length = 20, blank=False, null=False)
    inscricao = models.CharField('Inscrição estadual', max_length = 15, blank=False, null=False)
    nome = models.CharField('Nome fantasia', max_length = 70, blank=False, null=False)
    produto = models.CharField('Produto', max_length = 80, blank=False, null=False)
    endereco = models.CharField('Endereço', max_length = 50, blank=False, null=False)
    bairro = models.CharField('Bairro', max_length = 50, blank=False, null=False)
    cidade = models.CharField('Cidade', max_length = 50, blank=False, null=False)
    uf = models.CharField('Estado', max_length = 2, blank=False, null=False)
    cep = models.CharField('CEP', max_length = 9, blank=False, null=False)
    telefone = models.CharField('Telefone', max_length = 10, blank=False, null=False)
    email = models.CharField('E-mail', max_length = 50, blank=False, null=False)
    insercoes = models.CharField('Inserções', max_length=100, blank=False, null=False)
    tipo_insercao = models.CharField('Tipo de inserção', max_length=15, choices=TIPO_TEXTO, null=False, blank=False)
    pagamento = models.CharField('Tipo de pagamento', max_length=15, choices=TIPO_PAGAMENTO, null=False, blank=False)
    valor_total = models.CharField('Valor do contrato', max_length=12, blank=False, null=False)
    parcelas = models.CharField('Quantidade de parcelas', max_length=2, blank=False, null=False)
    valor_parcelas = models.CharField('Valor das parcelas', max_length=12, blank=False, null=False)
    vencimento = models.CharField('Dia do vencimento', max_length=2)
    observacoes = models.TextField('Observações', null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)    
    
