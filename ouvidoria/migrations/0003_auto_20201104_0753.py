# Generated by Django 3.1.2 on 2020-11-04 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ouvidoria', '0002_auto_20201104_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionario',
            name='reposta',
        ),
        migrations.AddField(
            model_name='pergunta',
            name='resposta',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ouvidoria.resposta'),
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='pergunta',
            field=models.TextField(blank=True, null=True),
        ),
    ]