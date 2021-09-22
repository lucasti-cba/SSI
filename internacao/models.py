from django.db import models

# Create your models here.

class Internacao_Painel(models.Model):
    nome = models.TextField(blank=False, null=False, unique=False)
    idade = models.TextField(blank=False, null=False, unique=False)
    convenio = models.TextField(blank=False, null=False, unique=False)
    leito = models.TextField(blank=False, null=False, unique=False)
    ala = models.TextField(blank=False, null=False, unique=False)
    medico = models.TextField(blank=True, null=True, unique=False)
    dieta = models.TextField(blank=True, null=True, unique=False)
    situacao = models.TextField(blank=True, null=True, unique=False)
    observacao = models.TextField(blank=True, null=True, unique=False)
    entrada = models.DateTimeField(blank=False, null=False)
    alta = models.TextField(blank=True, null=True)
    cor = models.TextField(blank=True)
    class Meta:
        ordering = ["ala", "leito"]
    def __str__(self):
        return self.nome

class Soro_Painel(models.Model):
    nome = models.TextField(blank=False, null=False, unique=False)
    leito = models.TextField(blank=False, null=False, unique=False)
    ala = models.TextField(blank=False, null=False, unique=False)
    situacao = models.TextField(blank=True, null=True, unique=False)
    entrada = models.DateTimeField(blank=False, null=False)
    alta = models.DateTimeField(blank=False, null=False)
    cor = models.TextField(blank=True)
    class Meta:
        ordering = ["ala", "leito"]
    def __str__(self):
        return self.nome
        
class Internacao_Painel_Tasy(models.Model):
    leito = models.TextField(blank=True, null=True, unique=True)
    codpac = models.TextField(blank=True, null=True, unique=False)
    convenio = models.IntegerField(blank=True, null=True, unique=False)
    medico = models.TextField(blank=True, null=True, unique=False)
    paciente = models.TextField(blank=True, null=True, unique=False)
    proce = models.TextField(blank=True, null=True, unique=False)
    alta = models.DateTimeField(blank=True, null=True, unique=False)
    observacao = models.TextField(blank=True, null=True, unique=False)
    entrada = models.DateTimeField(blank=True, null=True, unique=False)
    class Meta:
        ordering = ["leito"]


class Internacao_SAE(models.Model):
    paciente = models.ForeignKey(Internacao_Painel, on_delete=models.CASCADE, blank=True, null=True)
    exames = models.TextField(blank=True, null=True, unique=False)
    outros = models.TextField(blank=True, null=True, unique=False)
    alta = models.DateTimeField(blank=True, null=True)



class ProcedimentosPaMedicos(models.Model):
    medico = models.TextField(blank=True, null=True, unique=False)
    procedimento = models.TextField(blank=True, null=True, unique=False)
    data = models.DateTimeField(blank=True, null=True, unique=False)
    class Meta:
        ordering = ["data"]
