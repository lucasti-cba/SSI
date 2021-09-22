from django import forms
from .models import *

class NovaInternacao_Form(forms.Form):
	ALA_CHOICES = (('LC', 'LC'),('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'))
	LEITO_CHOICES = (('A', 'A'), ('B', 'B'), ('C', 'C'),  ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'),  ('J', 'J'))
	paciente =  forms.CharField(label='Paciente', max_length=250)
	idade = forms.CharField(label='Idade', max_length=3)
	convenio = forms.CharField(label='Convênio', max_length=30)
	situacao = forms.CharField(label='Situação', max_length=250)
	ala =  forms.ChoiceField(choices = ALA_CHOICES, label='Ala')
	leito =  forms.ChoiceField(choices = LEITO_CHOICES, label='Leito')
	medico =  forms.CharField(label='Medico', max_length=50) 
	dieta =  forms.CharField(label='Dieta', max_length=30)
	observacao =  forms.CharField(label='Observação', max_length=150)

class NovaSoro_Form(forms.Form):
	TEMPO_CHOICES = (('30 min', '30 min'),('60 min', '60 min'),('120 min', '120 min'), ('180 min', '180 min'),('240 min', '240 min'))
	ALA_CHOICES = (('Soro01', 'Soro01'),('Soro02', 'Soro02'),)
	LEITO_CHOICES = (('A', 'A'), ('B', 'B'), ('C', 'C'),  ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'),  ('J', 'J'))
	paciente =  forms.CharField(label='Paciente', max_length=250)
	ala =  forms.ChoiceField(choices = ALA_CHOICES, label='Ala')
	leito =  forms.ChoiceField(choices = LEITO_CHOICES, label='Leito')
	tempo =  forms.ChoiceField(choices = TEMPO_CHOICES, label='Tempo')

class Color_Form(forms.Form):
	COLOR_CHOICES = (('AZUL', 'AZUL'), ('VERDE', 'VERDE'), ('VERMELHO', 'VERMELHO'), ('LARANJA', 'LARANJA'))
	cor = forms.ChoiceField(choices = COLOR_CHOICES, label='Cor')


class Procurar(forms.Form):
	texto = forms.CharField(label='Pesquisa')


class SAE_Form(forms.ModelForm):
    EXAMES_CHOICES = (( 'TC', 'TC'), ('USG', 'USG'), ('EX. Labotariais', 'EX. Labotariais'), ('Outros', 'Outros'))
    exames = forms.MultipleChoiceField(label = 'Exames? ', widget=forms.CheckboxSelectMultiple, choices = EXAMES_CHOICES)
    outros = forms.CharField(label='Outros', max_length=250)
    alta = forms.DateField(widget=forms.SelectDateWidget())
    def __init__(self, *args, **kwargs):
        super(SAE_Form, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
	            'class': 'form-control',
            })

