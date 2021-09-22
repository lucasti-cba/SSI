from django import forms

class AddAlimento_Form(forms.Form):
	alimento = forms.CharField(label='Alimento', max_length=250)

class AddCardap_Form(forms.Form):
	title = forms.CharField(label='Titulo', max_length=50)
	data = forms.DateField(label='Data', widget=forms.SelectDateWidget)
	descricao = forms.CharField(label='Titulo', max_length=500)