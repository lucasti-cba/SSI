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

# Create your views here.
def indexo(request):
	pesquisas = Pesquisa.objects.all()
	return render(request, 'index_pesquisa.html', {'pesquisas':pesquisas})

def novaPesquisa(request):
	form = Perguntas_Form()
	if request.method == 'POST':
		form = Perguntas_Form(request.POST)
		if form.is_valid():
			titulo = form.cleaned_data['titulo']
			descricao = form.cleaned_data['descricao']
			pesquisa = Pesquisa(titulo = titulo, descricao = descricao)
			pesquisa.save()
			return redirect('indexo')
	return render(request, 'novaPesquisa.html', {'form':form})

def novaQuestao(request, id	):
	pesq = get_object_or_404(Pesquisa, id=id)	
	form = NovaQuestao()
	if request.method == 'POST':
		form = NovaQuestao(request.POST)
		if form.is_valid():
			questao = form.cleaned_data['questao']
			pergunta = Pergunta(pergunta = questao)
			pergunta.save()
			pesq.pergunta = pergunta
			pesq.save()
			return redirect('indexo')

	return render(request, 'novaQuestao.html', {'form':form, 'pesquisa':pesq })

def pesquisa(request, id ):
	pesquisa = get_object_or_404(Pesquisa, id=id)	
	return render(request, 'pesquisa_view.html', {'pesquisa':pesquisa})