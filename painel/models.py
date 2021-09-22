from django.db import models

class Senha(models.Model):
	senha = models.TextField(blank=True, null=True)
	local = models.TextField(blank=True, null=True)
	status = models.TextField(blank=True, null=True)
	guiche = models.TextField(blank=True, null=True)
	preferencial = models.TextField(blank=True, null=True)
	dataImp = models.DateTimeField(blank=True, null=True)
	dataCham = models.DateTimeField(blank=True, null=True)
	class Meta:
		ordering = ["id"]
		def __str__(self):
			return self.id


class Guiche(models.Model):
	guiche = models.TextField(blank=True, null=True)
	atendente = models.IntegerField(blank=True, null=True, unique=True)

class Triagem(models.Model):
    atendimento = models.TextField(blank=False, null = False)
    
class AtendimentoGuiche(models.Model):
	senha = models.ManyToManyField(Senha)
	guiche = models.ForeignKey(Guiche, on_delete=models.CASCADE, blank=True, null=True)
	dataAten = models.DateTimeField()

class GeraSenha(models.Model):
	senha = models.IntegerField(blank=True, null=True)

class DadosTriagem(models.Model):
	senha = models.ForeignKey(Senha, on_delete=models.CASCADE, blank=True, null=True)
	nome = models.TextField(blank=True, null=True)
	telefone = models.TextField(blank=True, null=True)
	idade = models.TextField(blank=True, null=True)
	tempAx = models.TextField(blank=True, null=True)
	freqCar = models.TextField(blank=True, null=True)
	freqResp = models.TextField(blank=True, null=True)
	satOx = models.TextField(blank=True, null=True)
	presArt = models.TextField(blank=True, null=True)
	dataCham = models.DateTimeField(blank=True, null=True)
	class Meta:
		ordering = ["senha"]
		def __str__(self):
			return self.nome


class Consultorio(models.Model):
	consultorio = models.TextField(blank=True, null=True)
	medico = models.IntegerField(blank=True, null=True)


class Consulta(models.Model):
	consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE, blank=True, null=True)
	paciente = models.ForeignKey(DadosTriagem, on_delete=models.CASCADE, blank=True, null=True)
	dataCham = models.DateTimeField(blank=True, null=True)
