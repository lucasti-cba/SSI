from django import forms

class DadosPessoais_Form(forms.Form):
    nome = forms.CharField(label='nome', max_length=250)
    telefone = forms.CharField(label="telefone", max_length=50)
    idade = forms.CharField(label='idade', max_length=3)
    tempAx = forms.CharField(label='Temp. Aux.', max_length=4)
    freqCar = forms.CharField(label='Freq. Card.', max_length=6)
    freqResp = forms.CharField(label='Freq. Resp.', max_length=8)
    satOx = forms.CharField(label='Sat. Oxim.', max_length=4)
    presArt = forms.CharField(label='Pre. Art.', max_length=8)

class AntendenteGuiche(forms.Form):
	GUICHE_CHOICES = (('PA-01', 'PA-01'), ('PA-02', 'PA-02'), ('PA-03', 'PA-03'), ('PA-04', 'PA-04'))
	guiche = forms.ChoiceField(choices = GUICHE_CHOICES, label='Guichê')

class medicoConsultorio(forms.Form):
    consultorio = forms.CharField(label='consultorio', max_length=30)