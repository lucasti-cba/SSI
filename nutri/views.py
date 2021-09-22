from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
	return render(request, 'indexn.html')

def cardapio(request):
	cardapios = Cardapio.objects.all()	
	return render(request, 'cardapio.html', {'cardapios':cardapios} )

def card_edit(request):
	form =  AddCardap_Form()
	if request.method == 'POST':
		print('Formulario postado')
		form =  AddCardap_Form(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			descricao = form.cleaned_data['descricao']
			data = form.cleaned_data['data']
			cardapio = Cardapio(title=title, descricao=descricao, data=data)
			cardapio.save()
	cardapios = Cardapio.objects.all()
	return render(request, 'card_edit.html', {'cardapios':cardapios})

def novarefe(request, id):
	cardapio = Cardapio.objects.get(pk=id)
	form = AddAlimento_Form()
	if request.method == 'POST':
		print('Formulario postado')
		form = AddAlimento_Form(request.POST)
		if form.is_valid():
			alimento = form.cleaned_data['alimento']
			ali = Alimento(nome=alimento)
			ali.save()
			cardapio.alimentos.add(ali)
			cardapio.save()
	return render(request, 'novarefe.html', {'form_add_alimento':form, 'cardapio':cardapio})

def removeAlimento(request, id, alimento):
	cardapio = Cardapio.objects.get(pk=id)
	alimentod = Alimento.objects.get(pk=alimento)
	alimentod.delete()
	return redirect('novarefe', 1)

def removeCardapio(request, id):
	cardapio = Cardapio.objects.get(pk=id)
	cardapio.delete()
	return redirect('card_edit')