from django import forms

class DadosPessoais_Form(forms.Form):
	nome = forms.CharField(label='nome', max_length=250)
	setor = forms.CharField(label="setor", max_length=50)
	cargo = forms.CharField(label='cargo', max_length=50)
	telefone = forms.CharField(label='telefone', max_length=15)
	email = forms.CharField(label='email', max_length=100)

class OrdemTi_Form(forms.Form):
	TIPO_CHOICES = (('Computador não liga, sem Internet ou Rede', 'Computador não liga, sem Internet ou Rede'), ('Problemas com office ou outro software', 'Problemas com office ou outro software'), ('Impressora não imprime ou digitaliza', 'Impressora não imprime ou digitaliza'), ('Impressão falhada ou erro de suprimento', 'Impressão falhada ou erro de suprimento'),('Cadastro InfoHosp', 'Cadastro InfoHosp'), ('Outros problemas', 'Outros problemas'))
	tipo = forms.ChoiceField(choices = TIPO_CHOICES)
	descricao = forms.CharField(label='descricao', max_length=500)

class OrdemManu_Form(forms.Form):
	TIPO_CHOICES = (('Predial - Eletrica - Hidraulica', 'Predial - Eletrica - Hidraulica' ), ('Equipamentos Tercerizados', 'Equipamentos Tercerizados'), ('Ar Condicionado', 'Ar Condicionado'))
	tipo = forms.ChoiceField(choices = TIPO_CHOICES)
	descricao = forms.CharField(label='descricao', max_length=500)

class Prioridade_Form(forms.Form):
	Prioridade_CHOICES = ((1, 'Sem prioridade'), (2, 'Urgente'), (3, 'Emergencial') )
	prioridade = forms.ChoiceField(choices= Prioridade_CHOICES)

class Ordemtiedit_Form(forms.Form):
	laudos = forms.CharField(label='laudos', max_length=1000)
	servicos = forms.CharField(label='servicos', max_length=1000)
	materiais = forms.CharField(label='materias', max_length=1000)


class Cadastro_InfoHosp_Form(forms.Form):
	ALT_CHOICES = ((True, 'SIM'), (False, 'NÃO') )
	nome = forms.CharField(label='Nome', max_length=150)
	nascimento = forms.CharField(label='Data de Nascimento', max_length=15)
	cpf = forms.CharField(label='CPF', max_length=15)
	rua = forms.CharField(label='Rua', max_length=150)
	numero = forms.CharField(label='Numero', max_length=10)
	bairro =  forms.CharField(label='Bairro', max_length=50)
	complemento = forms.CharField(label='Complemento', max_length=150)
	cidade = forms.CharField(label='Cidade', max_length=50)
	CEP = forms.CharField(label='CEP', max_length=10)
	medico = forms.ChoiceField(choices = ALT_CHOICES)
	crm_tipo = forms.CharField(label='Registro Tipo', max_length=3)
	crm_numero = forms.CharField(label='Registro', max_length=10)
	crm_espec = forms.CharField(label='Especialidade', max_length=50)
	consultorio  = forms.ChoiceField(choices = ALT_CHOICES)

class Create_produto(forms.Form):
	departamento = forms.CharField(label='Departamento', max_length=20)
	nome = forms.CharField(label='Nome', max_length=50)
	tipo_cont = forms.CharField(label='Unidade', max_length=5)
	codigo = forms.CharField(label='Codigo', max_length=20)
	descricao = forms.CharField(label='Descrição', max_length=500)
	imagem = forms.ImageField(label='Imagem', required=False)

class Edit_produto(forms.Form):
	nome = forms.CharField(label='Nome', max_length=50)
	tipo_cont = forms.CharField(label='Unidade', max_length=5)
	codigo = forms.CharField(label='Codigo', max_length=20)
	descricao = forms.CharField(label='Descrição', max_length=500)

class add_Imagem(forms.Form):
	imagem = forms.ImageField(label='Imagem', required=False)

class AddProdutoEstoque(forms.Form):
    quantidade = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Quantidade'}))