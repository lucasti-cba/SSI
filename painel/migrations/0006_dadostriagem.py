# Generated by Django 3.0.8 on 2020-07-22 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0005_gerasenha'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosTriagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.TextField(blank=True, null=True)),
                ('idade', models.TextField(blank=True, null=True)),
                ('tempAx', models.TextField(blank=True, null=True)),
                ('freqCar', models.TextField(blank=True, null=True)),
                ('freqResp', models.TextField(blank=True, null=True)),
                ('satOx', models.TextField(blank=True, null=True)),
                ('presArt', models.TextField(blank=True, null=True)),
                ('senha', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='painel.Senha')),
            ],
        ),
    ]