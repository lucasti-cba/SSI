from django.db import models

# Create your models here.

class Imagem(models.Model):
	imagens = models.ImageField(upload_to='images/', blank=True,null=True)

class Alimento(models.Model):
	nome = models.TextField(blank=False, null=False)

class Cardapio(models.Model):
	alimentos = models.ManyToManyField(Alimento)
	data = models.DateField()
	descricao = models.TextField(blank=False, null=False)
	title = models.TextField(blank=False, null=False)


class Presenca(models.Model):
	pessoa = models.IntegerField(blank=False, null=False)
	presenca = models.TextField(blank=False, null=False)
	data = models.DateField()

class Post(models.Model):
	title = models.TextField(blank=False, null=False)
	post = models.TextField(blank=False, null=False)
	data = models.DateField()

