# Generated by Django 3.1.2 on 2020-12-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0012_consulta_datacham'),
    ]

    operations = [
        migrations.CreateModel(
            name='Triagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atendimento', models.TextField()),
            ],
        ),
    ]