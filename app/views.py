from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from .models import *
from .forms import *
import os
import time
from django.template import Library
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime

register = Library()





@login_required(redirect_field_name='logar_usuario')
def compra(request, departamento, id):
    user = request.user.id    
    estoque = Estoque.objects.filter(depatarmento=departamento)
    querry = []
    img = []
    for iten in estoque:
        produto = Produto.objects.filter(id=iten.produto_id)
        querry += produto 
    busca = request.GET.get('search')
    if busca:
        querry = []
        for iten in estoque:
            produto = Produto.objects.filter(id=iten.produto_id, nome__icontains = busca ) or Produto.objects.filter(id=iten.produto_id, descricao__icontains = busca ) or Produto.objects.filter(id=iten.produto_id, codigo__icontains = busca )
            querry += produto 
    add = AddProdutoEstoque()
    notifi = findNotifications(user, 'Enviado')
    qnt_not = len(notifi)
    ordem = id
    return render(request, 'produtos_c.html', {'title':'Estoque','ordem':ordem,  'qnt_not':qnt_not, 'mensagem1':'Bem vindo ao Sistema de Gestão Interna', 'mensagem2':'Faça já seu registro clique no registrar acima.',  'querry':querry, 'estoque':estoque, 'add':add })



@login_required(redirect_field_name='logar_usuario')
def produtos(request, departamento):
    user = request.user.id    
    estoque = Estoque.objects.filter(depatarmento=departamento)
    querry = []
    busca = ''
    img = []
    cont = 0
    for iten in estoque:
        produto = Produto.objects.filter(id=iten.produto_id)
        querry += produto  
    add = AddProdutoEstoque()
    notifi = findNotifications(user, 'Enviado')
    qnt_not = len(notifi)
    busca = request.GET.get('search')
    if busca:
        querry = []        
        for iten in estoque:
            produto = Produto.objects.filter(id=iten.produto_id, nome__icontains = busca ) or Produto.objects.filter(id=iten.produto_id, descricao__icontains = busca ) or Produto.objects.filter(id=iten.produto_id, codigo__icontains = busca )
            querry += produto
            if produto:
                cont += 1
        busca = str(cont) +' resultados encontrados de '+ busca 

    return render(request, 'produtos.html', {'title':'Estoque','busca':busca, 'qnt_not':qnt_not, 'mensagem1':'Bem vindo ao Sistema de Gestão Interna', 'mensagem2':'Faça já seu registro clique no registrar acima.',  'querry':querry, 'estoque':estoque, 'add':add })

@login_required(redirect_field_name='logar_usuario')
def cadastrarProdutos(request):
    user = request.user.id    
    if request.method == 'POST':
        print('Formulario postado')
        form = Create_produto(request.POST, request.FILES)
        if form.is_valid():
            print('Formulario é valido')
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            tipo_cont = form.cleaned_data['tipo_cont']
            codigo = form.cleaned_data['codigo']
            imagem = form.cleaned_data['imagem']
            imagens = ImagemProduto(imagens=imagem) 
            imagens.save()                        
            departamento = form.cleaned_data['departamento']            
            produto = Produto(nome=nome.upper(), descricao=descricao,  codigo=codigo, tipo_cont=tipo_cont)
            produto.save()
            produto.imagens.add(imagens)
            produto.save()
            estoque = Estoque(quantidade=0, depatarmento=departamento, produto=produto)
            estoque.save()
            return redirect('index')
    notifi = findNotifications(user, 'Enviado')
    qnt_not = len(notifi)
    form_cadastro_produto = Create_produto()
    return render(request, 'cadastro_produtos.html', {'qnt_not':qnt_not, 'mensagem1':'Bem vindo ao Sistema de Gestão Interna', 'mensagem2':'Faça já seu registro clique no registrar acima.',  'form':form_cadastro_produto,  'title':'Criar novo produto', })

@login_required(redirect_field_name='logar_usuario')
def produto_update(request, id):
    user = request.user.id
    produto = get_object_or_404(Produto, pk=id)
    if request.method == 'POST':
        form = Edit_produto(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            codigo = form.cleaned_data['codigo']
            tipo_cont = form.cleaned_data['tipo_cont']
            produto = Produto(id=id, nome=nome.upper(), descricao=descricao, codigo=codigo, tipo_cont=tipo_cont)
            produto.save()
    form_edit_produto = Edit_produto()
    return render(request, 'editar_produtos.html', {'form':form_edit_produto, 'title':'Editar produto',  'produto':produto})

@login_required(redirect_field_name='logar_usuario')
def prodImagem_add(request, id):
    produto = get_object_or_404(Produto, pk=id)
    if request.method == 'POST':
        form = add_Imagem(request.POST, request.FILES)
        if form.is_valid():
            imagem = form.cleaned_data['imagem']
            imagens = ImagemProduto(imagens=imagem) 
            imagens.save()  
            produto.imagens.add(imagens)
            produto.save()   
    return render(request, 'editar_produtos.html', {'title':'Editar produto',  'produto':produto})

@login_required(redirect_field_name='logar_usuario')
def prodImagem_del(request, id, produto):
    imagem = get_object_or_404(ImagemProduto, pk=id)
    prod = get_object_or_404(Estoque, produto_id=produto)
    departamento = prod.depatarmento
    imagem.delete()
    return redirect('produtos', departamento)


@login_required(redirect_field_name='logar_usuario')
def produto_delete(request, id):
    produto = get_object_or_404(Produto, pk=id)
    departamento = Estoque.objects.get(produto_id = produto.id)
    produto.delete()
    return redirect('produtos', departamento.depatarmento)


@login_required(redirect_field_name='logar_usuario')
def produto_add(request, id):
    form = AddProdutoEstoque(request.POST)
    if form.is_valid():
        estoque = get_object_or_404(Estoque, pk=id)
        add = form.cleaned_data['quantidade']
        estoque.quantidade += add
        estoque.save()
    return redirect('produtos', estoque.depatarmento)


@login_required(redirect_field_name='logar_usuario')
def produto_addc(request, id, ordem):
    user = request.user.id
    form = AddProdutoEstoque(request.POST)
    if form.is_valid():
        estoque = get_object_or_404(Estoque, pk=id)
        add = form.cleaned_data['quantidade']
        estoque.quantidade += -add
        estoque.save()
        ordm = get_object_or_404(Ordem_ti, pk=ordem)
        produto = get_object_or_404(Produto, pk=  estoque.produto_id)
        if ordm.materiais  is None : ordm.materiais = '\n\n'+ str(add) + ' x ' + produto.nome 
        else: ordm.materiais += '\n\n'+ str(add) + ' x ' + produto.nome 
        ordm.save()
        compra = Compra(user=user, tipo='INTERNA', data_pedido= datetime.now(), status='FINALIZADA')
        compra.save()
        produtos = produtosCompra(quantidade=add)
        produtos.save()
        produtos.produtos.add(produto.id)
        produtos.save()
        compra.produtos.add(produtos)

    return redirect('compra', estoque.depatarmento, ordem)



def sendNotifications(tipo, user, descricao, setor):
	user_ = get_object_or_404(Dados_pessoais, user=user)
	if tipo == 'Nova Ordem':
		mensagem= 'Bom dia o colaborador '+user_.nome+' abriu uma nova Ordem de serviço, do setor '+user_.setor+' contato '+user_.telefone+', você possui uma nova Ordem , descrição da ordem : ---> '+descricao
		nova = Notificacoes(user=user, status='Não Lida', mensagem=mensagem, data=datetime.now(), contato=user_.telefone, setor=setor)
		nova.save()
	else:
		return 0

def findNotifications(user, status):
	notifi = Notificacoes.objects.filter(user=user, status=status)
	return notifi


def estoque(request):
	return render(request, "index.html",{'title': 'SSI' , 'mensagem1':'Bem vindo ao Sistema de Gestão Interna', 'mensagem2':'Faça já seu registro clique no registrar acima.' } )



# Create your views here.
def index(request):
	user = request.user.id
	notifi = findNotifications(user, 'Enviado')
	qnt_not = len(notifi)
	return render(request, "index.html",{'title': 'SSI' ,'qnt_not':qnt_not, 'mensagem1':'Bem vindo ao Sistema de Gestão Interna', 'mensagem2':'Faça já seu registro clique no registrar acima.' } )

def del_notifications(request, id):
	notifi = get_object_or_404(Notificacoes, id=id)
	notifi.delete()
	return redirect(view_notifications)

def lida_notifications(request, id):
	notifi = get_object_or_404(Notificacoes, id=id)
	notifi.status = 'Lida'
	return view_notifications


def delt_notifications(request, user):
	notifi = Notificacoes.objects.filter(user=user)
	for row in notifi:
		row.delete()		
	return redirect(view_notifications)

def lidat_notifications(request, user):
	notifi = Notificacoes.objects.filter(user=user)
	for row in notifi:
		row.status = 'Lida'	
	return view_notifications


def view_notifications(request):
	user = request.user.id
	notifi = findNotifications(user, 'Enviado')
	qnt_not = len(notifi)
	return render(request,"notifications.html", {'title': 'SSI' ,'notifications':notifi,'qnt_not':qnt_not, 'mensagem1':'Bem vindo ao Sistema de Gestão Interna', 'mensagem2':'Faça já seu registro clique no registrar acima.' } )



def cadastrar_usuario(request):
	if request.method == "POST":
	    form_usuario = UserCreationForm(request.POST)
	    if form_usuario.is_valid():
	        form_usuario.save()
	        username = form_usuario.cleaned_data['username']
	        password = form_usuario.cleaned_data['password1']
	        usuario = authenticate(request, username=username, password=password)
	        if usuario is not None:
	            auth_login(request, usuario)
	            return redirect('dadospessoais')
	    else:
	    	return render(request, 'cadastro_user.html', {'form': form_usuario, 'title': 'Criar Conta', })

	form = UserCreationForm()	
	return render(request, 'cadastro_user.html', {'form': form, 'title': 'Criar Conta', })




def logar_usuario(request):
    mensagem = None 
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            auth_login(request, usuario)
            user = request.user.id
            try:
	            dados = Dados_pessoais.objects.get(user=user)	         
	            return redirect('index')
            except:
            	return redirect('dadospessoais')
        else:
        	mensagem = 'Usuario ou senha invalido.'
    return render(request, 'user_login.html', {'mensagem':mensagem, 'title':'Login', })




def logout(request):
    auth_logout(request)
    return redirect('index')


@login_required(redirect_field_name='logar_usuario')
def dadospessoais(request):
	user = request.user.id
	if request.method == "POST":
		form = DadosPessoais_Form(request.POST)
		if form.is_valid():
			try:
				dados = Dados_pessoais.objects.filter(user=user)
				nome = form.cleaned_data['nome']
				setor = form.cleaned_data['setor']
				cargo = form.cleaned_data['cargo']
				telefone = form.cleaned_data['telefone']
				email = form.cleaned_data['email']
				dadosP = Dados_pessoais(id=dados[0].id, user=user,nome=nome, setor=setor, cargo=cargo, telefone=telefone, email=email)
				dadosP.save()
				return redirect("index")
			except:
				nome = form.cleaned_data['nome']
				setor = form.cleaned_data['setor']
				cargo = form.cleaned_data['cargo']
				telefone = form.cleaned_data['telefone']
				email = form.cleaned_data['email']
				dadosP = Dados_pessoais(user=user,nome=nome, setor=setor, cargo=cargo, telefone=telefone, email=email)
				dadosP.save()
				usern = request.user
				usern.groups.add(1)
				usern.save()
				return redirect("index")
	try:
		dados = Dados_pessoais.objects.filter(user=user)
		if dados[0] is None:
			pass
		form = DadosPessoais_Form()
		return render(request, 'dadospessoais.html', {'form': form, 'dados': dados[0], 'title': 'Editar Dados Pessais'})
	except:
		pass
	form = DadosPessoais_Form()
	return render(request, 'dadospessoais.html', {'form': form, 'title': 'Editar Dados Pessais', })




@login_required(redirect_field_name='logar_usuario')
def gerar_ordemti(request):
	user = request.user.id
	if request.method == "POST":
		print('Formulario Postado')
		form = OrdemTi_Form(request.POST)
		if form.is_valid():
			
			dados = Dados_pessoais.objects.filter(user=user)
			tipo = form.cleaned_data['tipo']
			descricao = form.cleaned_data['descricao']
			solicitante = dados[0].nome
			setor = dados[0].setor
			data = datetime.now()
			novaOrdem = Ordem_ti(solicitante=solicitante, user=user, setor=setor, tipo=tipo, status_ordem = 'ABERTA', data_solcitada=data, descricao=descricao, tempo_atendimento=0)
			novaOrdem.save()
			sendNotifications('Nova Ordem', user, descricao, 'TI')		
			return redirect('index')
	form = OrdemTi_Form()		
	return render(request, 'geraordemti.html', {'title':'Solicitar Nova Ordem de Serviço'})



@login_required(redirect_field_name='logar_usuario')
def gerar_ordemManu(request):
	user = request.user.id
	if request.method == "POST":
		print('Formulario Postado')
		form = OrdemManu_Form(request.POST)
		if form.is_valid():			
			dados = Dados_pessoais.objects.filter(user=user)
			tipo = form.cleaned_data['tipo']
			descricao = form.cleaned_data['descricao']
			solicitante = dados[0].nome
			setor = dados[0].setor
			data = datetime.now()
			if tipo == 'Predial - Eletrica - Hidraulica':
				novaOrdem = Ordem_Manu_predial(solicitante=solicitante, user=user, setor=setor, tipo=tipo, status_ordem = 'ABERTA', data_solcitada=data, descricao=descricao, tempo_atendimento=0)
				sendNotifications('Nova Ordem', user, descricao, 'MAN_P')
				novaOrdem.save()
			elif tipo ==  'Equipamentos Tercerizados':
				novaOrdem = Ordem_Manu_terceiri(solicitante=solicitante, user=user, setor=setor, tipo=tipo, status_ordem = 'ABERTA', data_solcitada=data, descricao=descricao, tempo_atendimento=0)
				sendNotifications('Nova Ordem', user, descricao, 'MAN_T')				
				novaOrdem.save()
			elif tipo == 'Ar Condicionado':
				novaOrdem = Ordem_Manu_arCond(solicitante=solicitante, user=user, setor=setor, tipo=tipo, status_ordem = 'ABERTA', data_solcitada=data, descricao=descricao, tempo_atendimento=0)
				sendNotifications('Nova Ordem', user, descricao, 'MAN_A')
				novaOrdem.save()
			return redirect('gerar_ordemManu')
	return render(request, 'geraordemManu.html', {'title':'Solicitar Nova Ordem de Serviço'})





@login_required(redirect_field_name='logar_usuario')
def ordemti_a(request):
	query = Ordem_ti.objects.filter(status_ordem='ABERTA')
	return render(request, 'ordemti_a.html', {'title':'Ordens em Aberto', 'query':query })




@login_required(redirect_field_name='logar_usuario')
def ordemManu_a(request):
	query1 = Ordem_Manu_predial.objects.filter(status_ordem='ABERTA')
	query2 = Ordem_Manu_terceiri.objects.filter(status_ordem='ABERTA')
	query3 = Ordem_Manu_arCond.objects.filter(status_ordem='ABERTA')	
	return render(request, 'ordemManu_a.html', {'title':'Ordens em Aberto', 'query1':query1, 'query2':query2, 'query3':query3   })




@login_required(redirect_field_name='logar_usuario')
def ordemti_f(request):
	query = Ordem_ti.objects.filter(status_ordem='FINALIZADA')
	return render(request, 'ordemti_f.html', {'title':'Ordens Finalizadas', 'query':query })




@login_required(redirect_field_name='logar_usuario')
def ordemManu_f(request):
	query1 = Ordem_Manu_predial.objects.filter(status_ordem='FINALIZADA')
	query2 = Ordem_Manu_terceiri.objects.filter(status_ordem='FINALIZADA')
	query3 = Ordem_Manu_arCond.objects.filter(status_ordem='FINALIZADA')
	return render(request, 'ordemManu_f.html', {'title':'Ordens Finalizadas', 'query1':query1, 'query2':query2, 'query3':query3 })




@login_required(redirect_field_name='logar_usuario')
def ordemti_cro(request):
	query = []	
	query += Ordem_ti.objects.filter(status_ordem='PAUSADA')
	query += Ordem_ti.objects.filter(status_ordem='ABERTA')
	queryi = Ordem_ti.objects.filter(status_ordem='EM PROGRESSO')
	return render(request, 'ordemti_c.html', {'title':'Cronograma de Atendimento', 'query':query,  'queryi':queryi  })




@login_required(redirect_field_name='logar_usuario')
def ordemManu_cro(request):
	query1 = []
	queryi = []	
	query1 += Ordem_Manu_predial.objects.filter(status_ordem='PAUSADA')
	query1 += Ordem_Manu_predial.objects.filter(status_ordem='ABERTA')
	queryi += Ordem_Manu_predial.objects.filter(status_ordem='EM PROGRESSO')
	query2 = []	
	query2 += Ordem_Manu_terceiri.objects.filter(status_ordem='PAUSADA')
	query2 += Ordem_Manu_terceiri.objects.filter(status_ordem='ABERTA')
	queryi += Ordem_Manu_terceiri.objects.filter(status_ordem='EM PROGRESSO')
	query3 = []	
	query3 += Ordem_Manu_arCond.objects.filter(status_ordem='PAUSADA')
	query3 += Ordem_Manu_arCond.objects.filter(status_ordem='ABERTA')
	queryi += Ordem_Manu_arCond.objects.filter(status_ordem='EM PROGRESSO')	
	return render(request, 'ordemManu_c.html', {'title':'Cronograma de Atendimento', 'query1':query1,  'query2':query2,  'query3':query3, 'queryi':queryi  })



@login_required(redirect_field_name='logar_usuario')
def ordemti_ini(request, id):
	user = request.user.id
	dados = Dados_pessoais.objects.filter(user=user)
	ordem = get_object_or_404(Ordem_ti, pk=id)
	ordem.data_concluida = datetime.now()
	ordem.status_ordem = 'EM PROGRESSO'
	ordem.atendente = dados[0].nome
	ordem.save()
	return redirect('ordemti_cro')



@login_required(redirect_field_name='logar_usuario')
def ordemManu_ini(request, id, tipo):
	user = request.user.id
	dados = Dados_pessoais.objects.filter(user=user)
	if tipo == 'Predial - Eletrica - Hidraulica' : ordem = get_object_or_404(Ordem_Manu_predial, pk=id)
	elif tipo == 'Equipamentos Tercerizados' : ordem = get_object_or_404(Ordem_Manu_terceiri, pk=id)
	elif tipo == 'Ar Condicionado' : ordem = get_object_or_404(Ordem_Manu_arCond, pk=id)
	ordem.data_concluida = datetime.now()
	ordem.status_ordem = 'EM PROGRESSO'
	ordem.atendente = dados[0].nome
	ordem.save()
	return redirect('ordemManu_cro')


@login_required(redirect_field_name='logar_usuario')
def ordemti_edit(request, id):
	user = request.user.id
	dados = Dados_pessoais.objects.filter(user=user)
	ordem = get_object_or_404(Ordem_ti, pk=id)
	if request.method == 'POST':
		form = Ordemtiedit_Form(request.POST)
		print(form)
		if form.is_valid:
			laudos = form.cleaned_data['laudos']
			servicos = form.cleaned_data['servicos']
			materiais = form.cleaned_data['materiais']
			ordem.laudos = laudos
			ordem.servico = servicos
			ordem.materiais = materiais
			ordem.save()
			return redirect('ordemti_cro')
	
	return render(request, 'ordemti_edit.html', {'title':'Editar Ordem Nº'+str(id), 'ordem':ordem })




@login_required(redirect_field_name='logar_usuario')
def ordemManu_edit(request, id, tipo):
	user = request.user.id
	dados = Dados_pessoais.objects.filter(user=user)
	if tipo == 'Predial - Eletrica - Hidraulica' : ordem = get_object_or_404(Ordem_Manu_predial, pk=id)
	elif tipo == 'Equipamentos Tercerizados' : ordem = get_object_or_404(Ordem_Manu_terceiri, pk=id)
	elif tipo == 'Ar Condicionado' : ordem = get_object_or_404(Ordem_Manu_arCond, pk=id)
	if request.method == 'POST':
		form = Ordemtiedit_Form(request.POST)
		print(form)
		if form.is_valid:
			laudos = form.cleaned_data['laudos']
			servicos = form.cleaned_data['servicos']
			materiais = form.cleaned_data['materiais']
			ordem.laudos = laudos
			ordem.servico = servicos
			ordem.materiais = materiais
			ordem.save()
			return redirect('ordemManu_cro')
	
	return render(request, 'ordemManu_edit.html', {'title':'Editar Ordem Nº'+str(id), 'ordem':ordem })




@login_required(redirect_field_name='logar_usuario')
def ordemManu_fim(request, id, tipo):
	if tipo == 'Predial - Eletrica - Hidraulica' : ordem = get_object_or_404(Ordem_Manu_predial, pk=id)
	elif tipo == 'Equipamentos Tercerizados' : ordem = get_object_or_404(Ordem_Manu_terceiri, pk=id)
	elif tipo == 'Ar Condicionado' : ordem = get_object_or_404(Ordem_Manu_arCond, pk=id)
	ordemtemp = ordem.data_concluida
	if ordem.tempo_atendimento == None: horatemp = 0
	else: horatemp = ordem.tempo_atendimento
	temp = []
	hora = int(ordemtemp[11:13])
	minuto = int(ordemtemp[14:16])	
	ordem.data_concluida = datetime.now()
	hora2 = datetime.now().hour
	hora2 = int(hora2)
	minuto2 = datetime.now().minute
	minuto2 = int(minuto2)
	hora = hora2 - hora 
	minuto = minuto2 - minuto
	if minuto > 0:
		minuto = minuto + 60
		hora = hora - 1
	horagasta = int(horatemp) + minuto + (hora * 60)
	ordem.status_ordem = 'FINALIZADA'
	ordem.tempo_atendimento = horagasta
	ordem.save()
	return redirect('ordemManu_cro')



@login_required(redirect_field_name='logar_usuario')
def ordemti_fim(request, id):
	ordem = get_object_or_404(Ordem_ti, pk=id)
	ordemtemp = ordem.data_concluida
	if ordem.tempo_atendimento == None: horatemp = 0
	else: horatemp = ordem.tempo_atendimento
	temp = []
	hora = int(ordemtemp[11:13])
	minuto = int(ordemtemp[14:16])	
	ordem.data_concluida = datetime.now()
	hora2 = datetime.now().hour
	hora2 = int(hora2)
	minuto2 = datetime.now().minute
	minuto2 = int(minuto2)
	hora = hora2 - hora 
	minuto = minuto2 - minuto
	if minuto > 0:
		minuto = minuto + 60
		hora = hora - 1
	horagasta = int(horatemp) + minuto + (hora * 60)
	ordem.status_ordem = 'FINALIZADA'
	ordem.tempo_atendimento = horagasta
	ordem.save()
	return redirect('compra', 'Ti', ordem.id)	


@login_required(redirect_field_name='logar_usuario')
def ordemManu_paus(request, id, tipo):
	if tipo == 'Predial - Eletrica - Hidraulica' : ordem = get_object_or_404(Ordem_Manu_predial, pk=id)
	elif tipo == 'Equipamentos Tercerizados' : ordem = get_object_or_404(Ordem_Manu_terceiri, pk=id)
	elif tipo == 'Ar Condicionado' : ordem = get_object_or_404(Ordem_Manu_arCond, pk=id)
	ordemtemp = ordem.data_concluida
	horatemp = ordem.tempo_atendimento
	temp = []
	hora = int(ordemtemp[11:13])
	minuto = int(ordemtemp[14:16])	
	ordem.data_concluida = datetime.now()
	hora2 = datetime.now().hour
	hora2 = int(hora2)
	minuto2 = datetime.now().minute
	minuto2 = int(minuto2)
	hora = hora2 - hora 
	minuto = minuto2 - minuto
	if minuto > 0:
		minuto = minuto + 60
		hora = hora - 1
	if horatemp == None : horatemp = 0
	horagasta = int(horatemp) + minuto + (hora * 60)
	ordem.status_ordem = 'PAUSADA'
	ordem.tempo_atendimento = str(horagasta)
	ordem.save()
	return redirect('ordemManu_cro')



@login_required(redirect_field_name='logar_usuario')
def ordemti_paus(request, id):
	ordem = get_object_or_404(Ordem_ti, pk=id)
	ordemtemp = ordem.data_concluida
	horatemp = ordem.tempo_atendimento
	temp = []
	hora = int(ordemtemp[11:13])
	minuto = int(ordemtemp[14:16])	
	ordem.data_concluida = datetime.now()
	hora2 = datetime.now().hour
	hora2 = int(hora2)
	minuto2 = datetime.now().minute
	minuto2 = int(minuto2)
	hora = hora2 - hora 
	minuto = minuto2 - minuto
	if minuto > 0:
		minuto = minuto + 60
		hora = hora - 1
	if horatemp == None : horatemp = 0
	horagasta = int(horatemp) + minuto + (hora * 60)
	ordem.status_ordem = 'PAUSADA'
	ordem.tempo_atendimento = str(horagasta)
	ordem.save()
	return redirect('ordemti_cro')




@login_required(redirect_field_name='logar_usuario')
def ordemManu_paus(request, id, tipo):
	if tipo == 'Predial - Eletrica - Hidraulica' : ordem = get_object_or_404(Ordem_Manu_predial, pk=id)
	elif tipo == 'Equipamentos Tercerizados' : ordem = get_object_or_404(Ordem_Manu_terceiri, pk=id)
	elif tipo == 'Ar Condicionado' : ordem = get_object_or_404(Ordem_Manu_arCond, pk=id)
	ordemtemp = ordem.data_concluida
	horatemp = ordem.tempo_atendimento
	temp = []
	hora = int(ordemtemp[11:13])
	minuto = int(ordemtemp[14:16])	
	ordem.data_concluida = datetime.now()
	hora2 = datetime.now().hour
	hora2 = int(hora2)
	minuto2 = datetime.now().minute
	minuto2 = int(minuto2)
	hora = hora2 - hora 
	minuto = minuto2 - minuto
	if minuto > 0:
		minuto = minuto + 60
		hora = hora - 1
	if horatemp == None : horatemp = 0
	horagasta = int(horatemp) + minuto + (hora * 60)
	ordem.status_ordem = 'PAUSADA'
	ordem.tempo_atendimento = str(horagasta)
	ordem.save()
	return redirect('ordemManu_cro')





@login_required(redirect_field_name='logar_usuario')
def vis_ordemti(request, id):
	ordem = get_object_or_404(Ordem_ti, pk=id)
	return render(request, 'vis_ordemti.html', {'title':'Ordem Nº '+ str(id), 'ordem':ordem})



@login_required(redirect_field_name='logar_usuario')
def vis_ordemManu(request, id, tipo):
	if tipo == 'Predial - Eletrica - Hidraulica' : ordem = get_object_or_404(Ordem_Manu_predial, pk=id)
	elif tipo == 'Equipamentos Tercerizados' : ordem = get_object_or_404(Ordem_Manu_terceiri, pk=id)
	elif tipo == 'Ar Condicionado' : ordem = get_object_or_404(Ordem_Manu_arCond, pk=id)
	return render(request, 'vis_ordemti.html', {'title':'Ordem Nº '+ str(id), 'ordem':ordem})



@login_required(redirect_field_name='logar_usuario')
def del_ordemti(request, id):
	ordem = get_object_or_404(Ordem_ti, pk=id)
	ordem.delete()
	return redirect('ordemti_a')

@login_required(redirect_field_name='logar_usuario')
def del_ordemManu(request, id, tipo):
	if tipo == 'Predial - Eletrica - Hidraulica' : ordem = get_object_or_404(Ordem_Manu_predial, pk=id)
	elif tipo == 'Equipamentos Tercerizados' : ordem = get_object_or_404(Ordem_Manu_terceiri, pk=id)
	elif tipo == 'Ar Condicionado' : ordem = get_object_or_404(Ordem_Manu_arCond, pk=id)
	ordem.delete()
	return redirect('ordemManu_a')



@login_required(redirect_field_name='logar_usuario')
def edit_pri_ordemti(request, id):
	if request.method == 'POST':
		form = Prioridade_Form(request.POST)
		if form.is_valid():
			print('fomulario validor')
			prioridade = form.cleaned_data['prioridade']
			ordem = get_object_or_404(Ordem_ti, pk=id)
			print(prioridade , ordem)
			ordem.prioridade = prioridade
			ordem.save()
	return redirect('ordemti_a')

@login_required(redirect_field_name='logar_usuario')
def edit_pri_ordemManu(request, id, tipo):
	if request.method == 'POST':
		form = Prioridade_Form(request.POST)
		if form.is_valid():
			print('fomulario validor')
			prioridade = form.cleaned_data['prioridade']
			if tipo == 'Predial - Eletrica - Hidraulica' : ordem = get_object_or_404(Ordem_Manu_predial, pk=id)
			elif tipo == 'Equipamentos Tercerizados' : ordem = get_object_or_404(Ordem_Manu_terceiri, pk=id)
			elif tipo == 'Ar Condicionado' : ordem = get_object_or_404(Ordem_Manu_arCond, pk=id)
			print(prioridade , ordem)
			ordem.prioridade = prioridade
			ordem.save()
	return redirect('ordemManu_a')



@login_required(redirect_field_name='logar_usuario')
def cadastro_infohosp(request):
	user = request.user.id
	dados = Dados_pessoais.objects.filter(user=user)
	if request.method == "POST":
		form = Cadastro_InfoHosp_Form(request.POST)
		if form.is_valid():
			tipo = 'Cadastro InfoHosp'
			descricao = 'Cadastro InfoHosp'
			nome = form.cleaned_data['nome']
			nascimento = form.cleaned_data['nascimento']
			cpf = form.cleaned_data['cpf']
			rua = form.cleaned_data['rua']
			numero = form.cleaned_data['numero']
			bairro =  form.cleaned_data['bairro']
			complemento = form.cleaned_data['complemento']
			cidade = form.cleaned_data['cidade']
			CEP = form.cleaned_data['CEP']
			medico = form.cleaned_data['medico']
			crm_tipo = form.cleaned_data['crm_tipo']
			crm_numero = form.cleaned_data['crm_numero']
			crm_espec = form.cleaned_data['crm_espec']
			consultorio  = form.cleaned_data['consultorio']
			if medico == 'True':
				medico = True
				if consultorio == 'True':
					consultorio = True
				else:
					consultorio = False
			else:
				medico = False
			ordem = Ordem_ti(solicitante=dados[0].nome, user = user, setor=dados[0].setor, tipo=tipo, data_solcitada= datetime.now(), status_ordem='ABERTA', descricao=descricao )
			ordem.save()
			cadastro = Cadastro_InfoHosp(nome=nome, nascimento=nascimento, cpf=cpf, rua=rua, numero=numero, bairro=bairro, complemento=complemento, cidade=cidade, CEP=CEP, medico=medico, crm_tipo=crm_tipo,crm_numero=crm_numero,crm_espec=crm_espec, consultorio=consultorio, ordem=ordem )
			cadastro.save()
			sendNotifications('Nova Ordem', user, descricao, 'TI')
			return redirect('ordemti_a')			
	return render(request, 'cadastro_infohosp.html', {'title':'Cadastro InfoHosp'})

@login_required(redirect_field_name='logar_usuario')
def cadastro_infohosp_vis(request, id):
	user = request.user.id
	dados = Dados_pessoais.objects.filter(user=user)
	cadastro = get_object_or_404(Cadastro_InfoHosp, ordem=id)
	return render(request, 'cadastro_infohosp_vis.html', {'title':'Cadastro InfoHosp Dados', 'cadastro':cadastro})

