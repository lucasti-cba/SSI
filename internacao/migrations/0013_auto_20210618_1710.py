# Generated by Django 3.1.2 on 2021-06-18 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internacao', '0012_internacao_painel_tasy_entrada'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='internacao_painel_tasy',
            options={'ordering': ['leito']},
        ),
    ]
