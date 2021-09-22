from django.db import models

# Create your models here.

class Pesquisa(models.Model):
	paciente = models.TextField(blank=True, null=True)
	quarto = models.TextField(blank=True, null=True)
	tria_1 = models.IntegerField(blank=True, null=True)
	tria_2 = models.IntegerField(blank=True, null=True)
	tria_3 = models.IntegerField(blank=True, null=True)
	rec_1 = models.IntegerField(blank=True, null=True)
	rec_2 = models.IntegerField(blank=True, null=True)
	eqmed_1 = models.IntegerField(blank=True, null=True)
	eqmed_2 = models.IntegerField(blank=True, null=True)
	eqmed_3 = models.IntegerField(blank=True, null=True)
	eqenf_1 = models.IntegerField(blank=True, null=True)
	eqenf_2 = models.IntegerField(blank=True, null=True)
	eqenf_3 = models.IntegerField(blank=True, null=True)
	eqenf_4 = models.IntegerField(blank=True, null=True)
	hig_1 = models.IntegerField(blank=True, null=True)
	hig_2 = models.IntegerField(blank=True, null=True)
	hig_3 = models.IntegerField(blank=True, null=True)
	hig_4 = models.IntegerField(blank=True, null=True)
	servi_1 = models.IntegerField(blank=True, null=True)
	servi_2 = models.IntegerField(blank=True, null=True)
	servi_3 = models.IntegerField(blank=True, null=True)
	outros_1 = models.IntegerField(blank=True, null=True)
	outros_2 = models.IntegerField(blank=True, null=True)
	rz_esc = models.IntegerField(blank=True, null=True)
	vol_util = models.IntegerField(blank=True, null=True)


