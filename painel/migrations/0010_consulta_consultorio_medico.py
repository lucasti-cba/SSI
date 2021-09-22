# Generated by Django 3.0.8 on 2020-07-25 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0009_auto_20200723_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultorio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultorio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='painel.Consultorio')),
                ('medico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='painel.Medico')),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='painel.DadosTriagem')),
            ],
        ),
    ]
