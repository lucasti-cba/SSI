# Generated by Django 3.1.2 on 2020-11-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internacao', '0002_auto_20201130_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internacao_Painel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(unique=True)),
                ('idade', models.TextField()),
                ('convenio', models.TextField()),
                ('leito', models.TextField(unique=True)),
                ('ala', models.TextField(unique=True)),
                ('medico', models.TextField(blank=True, null=True)),
                ('dieta', models.TextField(blank=True, null=True)),
                ('situacao', models.TextField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('entrada', models.DateTimeField()),
                ('alta', models.TextField(blank=True, null=True)),
                ('cor', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Internacao',
        ),
    ]
