# Generated by Django 3.1.2 on 2020-11-04 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ouvidoria', '0003_auto_20201104_0753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='paciente',
        ),
        migrations.AddField(
            model_name='resposta',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ouvidoria.paciente'),
        ),
    ]
