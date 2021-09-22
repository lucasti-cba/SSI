from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.

class ImagemProduto(models.Model):
	imagens = models.ImageField(upload_to='images/', blank=True,null=True)	


class Produto(models.Model):
	nome = models.TextField(blank=False, null=False)
	tipo_cont = models.TextField(blank=False, null=False)
	codigo = models.TextField(blank=False, null=False)
	descricao = models.TextField(blank=False, null=False)
	imagens = models.ManyToManyField(ImagemProduto)
	class Meta:
		ordering = ["nome"]
	def __str__(self):
		return self.nome

class Estoque(models.Model):
	depatarmento =  models.TextField(blank=True, null=True)
	produto = models.ForeignKey(Produto, on_delete=models.CASCADE, blank=True, null=True)
	quantidade = models.IntegerField(null=False, blank=False)	
	class Meta:
		ordering = ["produto"]
	def __str__(self):
		return self.produto.nome	

class produtosCompra(models.Model):
	produtos = models.ManyToManyField(Produto)
	quantidade = models.IntegerField(null=False, blank=False)

class Compra(models.Model):
	user = models.IntegerField(null=False, blank=False)	
	tipo = models.TextField(null=True, blank=True)
	data_pedido = models.DateTimeField()
	status = models.TextField(null=True, blank=True)
	produtos = models.ManyToManyField(produtosCompra)


class Dados_pessoais(models.Model):
	user = models.IntegerField(null=False, blank=False)
	nome = models.TextField(blank=False, null=False)
	setor = models.TextField(blank=False, null=False)
	cargo = models.TextField(blank=False, null=False)
	telefone = models.TextField(blank=False, null=False)
	email = models.TextField(blank=False, null=False)

class Notificacoes(models.Model):
	user = models.IntegerField(null=True, blank=True)
	status =  models.TextField(blank=True, null=True)
	mensagem =  models.TextField(blank=True, null=True)
	data =  models.TextField(blank=True, null=True)
	contato = models.TextField(blank=True, null=True)
	setor = models.TextField(blank=True, null=True)


class Ordem_ti(models.Model):
	solicitante = models.TextField(blank=False, null=False)
	user = models.IntegerField(null=False, blank=False)
	setor = models.TextField(blank=False, null=False)
	tipo = models.TextField(null=True, blank=True)
	atendente = models.TextField(blank=True, null=True)
	data_solcitada = models.TextField(blank=False, null=False)
	data_concluida = models.TextField(blank=True, null=True)
	status_ordem = models.TextField(blank=False, null=False)
	descricao = models.TextField(blank=False, null=False)
	tempo_atendimento = models.TextField(blank=True, null=True)
	laudos = models.TextField(blank=True, null=True)
	servico = models.TextField(blank=True, null=True)
	materiais = models.TextField(blank=True, null=True)
	prioridade = models.IntegerField(null=True, blank=True)
	class Meta:
		ordering = ["id"]

class Cadastro_InfoHosp(models.Model):
	nome = models.TextField(blank=False, null=False)
	nascimento = models.TextField(blank=False, null=False)
	cpf = models.TextField(blank=False, null=False)
	rua = models.TextField(blank=True, null=True)
	numero = models.TextField(blank=True, null=True)
	bairro =  models.TextField(blank=True, null=True)
	complemento = models.TextField(blank=True, null=False)
	cidade = models.TextField(blank=True, null=True)
	CEP = models.TextField(blank=True, null=True)
	medico = models.BooleanField()
	crm_tipo = models.TextField(blank=True, null=True)
	crm_numero = models.TextField(blank=True, null=True)
	crm_espec = models.TextField(blank=True, null=True)
	consultorio  = models.BooleanField()
	ordem = models.ForeignKey(Ordem_ti, on_delete=models.CASCADE, blank=True, null=True)


class Ordem_Manu_predial(models.Model):
	solicitante = models.TextField(blank=False, null=False)
	user = models.IntegerField(null=False, blank=False)
	setor = models.TextField(blank=False, null=False)
	tipo = models.TextField(null=True, blank=True)
	atendente = models.TextField(blank=True, null=True)
	data_solcitada = models.TextField(blank=False, null=False)
	data_concluida = models.TextField(blank=True, null=True)
	status_ordem = models.TextField(blank=False, null=False)
	descricao = models.TextField(blank=False, null=False)
	tempo_atendimento = models.TextField(blank=True, null=True)
	laudos = models.TextField(blank=True, null=True)
	servico = models.TextField(blank=True, null=True)
	materiais = models.TextField(blank=True, null=True)
	prioridade = models.IntegerField(null=True, blank=True)
	class Meta:
		ordering = ["id"]

class Ordem_Manu_terceiri(models.Model):
	solicitante = models.TextField(blank=False, null=False)
	user = models.IntegerField(null=False, blank=False)
	setor = models.TextField(blank=False, null=False)
	tipo = models.TextField(null=True, blank=True)
	atendente = models.TextField(blank=True, null=True)
	data_solcitada = models.TextField(blank=False, null=False)
	data_concluida = models.TextField(blank=True, null=True)
	status_ordem = models.TextField(blank=False, null=False)
	descricao = models.TextField(blank=False, null=False)
	tempo_atendimento = models.TextField(blank=True, null=True)
	laudos = models.TextField(blank=True, null=True)
	servico = models.TextField(blank=True, null=True)
	materiais = models.TextField(blank=True, null=True)
	prioridade = models.IntegerField(null=True, blank=True)
	class Meta:
		ordering = ["id"]

class Ordem_Manu_arCond(models.Model):
	solicitante = models.TextField(blank=False, null=False)
	user = models.IntegerField(null=False, blank=False)
	setor = models.TextField(blank=False, null=False)
	tipo = models.TextField(null=True, blank=True)
	atendente = models.TextField(blank=True, null=True)
	data_solcitada = models.TextField(blank=False, null=False)
	data_concluida = models.TextField(blank=True, null=True)
	status_ordem = models.TextField(blank=False, null=False)
	descricao = models.TextField(blank=False, null=False)
	tempo_atendimento = models.TextField(blank=True, null=True)
	laudos = models.TextField(blank=True, null=True)
	servico = models.TextField(blank=True, null=True)
	materiais = models.TextField(blank=True, null=True)
	prioridade = models.IntegerField(null=True, blank=True)
	class Meta:
		ordering = ["id"]

