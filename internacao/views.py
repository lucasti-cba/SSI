from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta, time
from .models import *
from .forms import *
from .bridge import getdados as gd 

# Create your views here.
def atualiza_painel(request):
    data = gd()
    for row in data:
        try:
            query = ProcedimentosPaMedicos(id = row[4], medico = row[1], procedimento = row[2], data = row[3])
            query.save()
        except:
            pass
    return render(request, 'update.html')

def internacao(request):
    internados = Internacao_Painel.objects.all()
    form = Color_Form()
    clinico = 0
    cirurgico = 0
    for inter in internados:
        if inter.situacao ==  'CLÍNICO': clinico += 1
        elif inter.situacao == 'CIRÚRGICO': cirurgico += 1
    return render(request, 'internacao.html', {'internados':internados,'cirurgico':cirurgico, 'clinico':clinico, 'form':form})


def soro(request):
    internados = Soro_Painel.objects.all()
    form = Color_Form()
    return render(request, 'soro.html', {'internados':internados,'form':form})


def internacaoV(request):
    internados = Internacao_Painel.objects.all()
    form = Color_Form()
    clinico = 0
    cirurgico = 0
    for inter in internados:
        if inter.situacao ==  'CLÍNICO': clinico += 1
        elif inter.situacao == 'CIRÚRGICO': cirurgico += 1
    return render(request, 'internacaoV.html', {'internados':internados,'cirurgico':cirurgico, 'clinico':clinico, 'form':form})


def check_Internacao(ala, leito):
    responder = False
    inter = get_object_or_404(Internacao_Painel, ala=ala, leito=leito, alta = 'I')
    if inter != None: responder = True
    return responder

def check_Soro(ala, leito):
    responder = False
    inter = get_object_or_404(Soro_Painel, ala=ala, leito=leito, alta = 'I')
    if inter != None: responder = True
    return responder

def add_internacao(request):
    form = NovaInternacao_Form()
    if request.method == 'POST':
        form = NovaInternacao_Form(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['paciente']
            idade = form.cleaned_data['idade']
            convenio = form.cleaned_data['convenio']
            situacao = form.cleaned_data['situacao']
            medico = form.cleaned_data['medico']
            dieta = form.cleaned_data['dieta']
            observacao = form.cleaned_data['observacao']
            ala = form.cleaned_data['ala']
            leito = form.cleaned_data['leito']
            if situacao.upper() == 'CLÍNICO': cor = 'AZUL'
            elif situacao.upper() == 'CIRÚRGICO': cor = 'VERDE'
            try: check = check_Internacao(ala, leito)
            except:
                internacaoM = Internacao_Painel(nome = nome.upper(), idade = idade, convenio = convenio.upper(), medico = medico.upper(), dieta = dieta, observacao = observacao,  ala= ala, cor = cor,  situacao = situacao , leito = leito.upper() , alta='I',  entrada = datetime.now())
                internacaoM.save()
                return redirect('internacao')
            if check == False:
                internacaoM = Internacao_Painel(nome = nome.upper(), idade = idade, convenio = convenio.upper(), medico = medico.upper(), dieta = dieta, observacao = observacao,  ala= ala, cor = cor,  situacao = situacao , leito = leito.upper() , alta='I',  entrada = datetime.now())
                internacaoM.save()
            else:
                return render(request, 'mensagem_erro_ala.html', {'ala':ala, 'leito':leito})

            return redirect('internacao')
    return render(request, 'nova_internacao.html', {'form':form} )

def add_soro(request):
    form = NovaSoro_Form()
    if request.method == 'POST':
        form = NovaSoro_Form(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['paciente']
            ala = form.cleaned_data['ala']
            leito = form.cleaned_data['leito']
            tempo = form.cleaned_data['tempo']
            if tempo == '30 min': alta = datetime.now() + timedelta(minutes=30)
            elif tempo == '60 min': alta = datetime.now() + timedelta(minutes=60)
            elif tempo == '120 min': alta = datetime.now() + timedelta(minutes=120)
            elif tempo == '180 min': alta = datetime.now() + timedelta(minutes=180)
            try: check = check_Soro(ala, leito)

            except:
                internacaoM = Soro_Painel(nome = nome.upper(),  ala= ala, cor = 'verde',  leito = leito.upper() , alta=alta,  entrada = datetime.now())
                internacaoM.save()
                return redirect('soro')
            if check == False:
                internacaoM = Soro_Painel(nome = nome.upper(), ala= ala, cor = 'verde',   leito = leito.upper() , alta=alta,  entrada = datetime.now())
                internacaoM.save()
            else:
                return render(request, 'mensagem_erro_ala.html', {'ala':ala, 'leito':leito})

            return redirect('soro')
    return render(request, 'nova_soro.html', {'form':form} )

def delete_internacao(request, id):
    inter = get_object_or_404(Internacao_Painel, id = id)
    inter.delete()
    return redirect('internacao')

def livre_internacao(request, id):
    inter = get_object_or_404(Internacao_Painel, id = id)
    interm = Internacao_Painel(id=inter.id,  nome='LIVRE', idade='LIVRE', convenio = 'LIVRE', medico='LIVRE', dieta = 'LIVRE', observacao = 'LIVRE', situacao = 'LIVRE', ala = inter.ala, leito = inter.leito, cor = 'CINZA', alta = 'I', entrada = datetime.now())
    interm.save()
    return redirect('internacao')

def reservado_internacao(request, id):
    inter = get_object_or_404(Internacao_Painel, id = id)
    interm = Internacao_Painel(id=inter.id,  nome='RESERVADO', idade='RESERVADO', convenio = 'RESERVADO', medico='RESERVADO', dieta = 'RESERVADO', observacao = 'LIVRE', situacao = 'RESERVADO', ala = inter.ala, leito = inter.leito, cor = 'LARANJA', alta = 'I', entrada = datetime.now())
    interm.save()
    return redirect('internacao')

def delete(id):
    inter = get_object_or_404(Internacao_Painel, id = id)
    inter.delete()

def edit_internacao(request, id):
    inter = get_object_or_404(Internacao_Painel, id = id)
    form = NovaInternacao_Form()
    if request.method == 'POST':
        form = NovaInternacao_Form(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['paciente']
            idade = form.cleaned_data['idade']
            convenio = form.cleaned_data['convenio']
            situacao = form.cleaned_data['situacao']
            medico = form.cleaned_data['medico']
            dieta = form.cleaned_data['dieta']
            observacao = form.cleaned_data['observacao']
            ala = form.cleaned_data['ala']
            leito = form.cleaned_data['leito']
            if situacao.upper() == 'CLÍNICO': cor = 'AZUL'
            elif situacao.upper() == 'CIRÚRGICO': cor = 'VERDE'
            try: check = check_Internacao(ala, leito)
            except:
                internacaoM = Internacao_Painel(id = id, nome = nome.upper(), idade = idade, convenio = convenio.upper(), medico = medico.upper(), dieta = dieta, observacao = observacao,  ala= ala, cor = cor,  situacao = situacao , leito = leito.upper() , alta='I',  entrada = datetime.now())
                internacaoM.save() 
                return redirect('internacao')                
            if check == False or ala == inter.ala and leito  == inter.leito:
                internacaoM = Internacao_Painel(id = id, nome = nome.upper(), idade = idade, convenio = convenio.upper(), medico = medico.upper(), dieta = dieta, observacao = observacao,  ala= ala, cor = cor,  situacao = situacao , leito = leito.upper() , alta='I',  entrada = datetime.now())
                internacaoM.save()
                return redirect('internacao')
            else:
                return render(request, 'mensagem_erro_ala.html', {'ala':ala, 'leito':leito})
    return render(request, 'edit_internacao.html', { 'inter':inter })


def colorPI(request, id):
    internacao = get_object_or_404(Internacao_Painel, id=id)
    form = Color_Form()
    if request.method == 'POST':
        form = Color_Form(request.POST)
        if form.is_valid():
            cor = form.cleaned_data['cor']
            print(cor)
            internacao.cor = cor
            internacao.save()
    return redirect('internacao')
