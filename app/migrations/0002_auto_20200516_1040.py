# Generated by Django 3.0.6 on 2020-05-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordem_ti',
            name='laudos',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordem_ti',
            name='prioridade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordem_ti',
            name='tipo',
            field=models.TextField(),
        ),
    ]