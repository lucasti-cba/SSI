# Generated by Django 3.0.6 on 2020-06-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200602_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacoes',
            name='setor',
            field=models.TextField(blank=True, null=True),
        ),
    ]