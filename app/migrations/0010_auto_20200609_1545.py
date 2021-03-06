# Generated by Django 3.0.6 on 2020-06-09 19:45

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200609_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ['nome']},
        ),
        migrations.AddField(
            model_name='produto',
            name='imagens',
            field=models.ImageField(blank=True, null=True, upload_to=django.core.files.storage.FileSystemStorage(location='/media/img//Produtos.id'), verbose_name='Imagens'),
        ),
    ]
