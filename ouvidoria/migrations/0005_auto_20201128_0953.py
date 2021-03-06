# Generated by Django 3.1.2 on 2020-11-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ouvidoria', '0004_auto_20201104_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pergunta',
            name='resposta',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='pergunta',
        ),
        migrations.RemoveField(
            model_name='resposta',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='questionario',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='titulo',
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='eqenf_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='eqenf_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='eqenf_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='eqenf_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='eqmed_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='eqmed_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='eqmed_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='hig_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='hig_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='hig_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='hig_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='outros_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='outros_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='paciente',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='quarto',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='rec_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='rec_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='rz_esc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='servi_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='servi_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='servi_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='tria_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='tria_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='tria_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='vol_util',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
        migrations.DeleteModel(
            name='Pergunta',
        ),
        migrations.DeleteModel(
            name='Questionario',
        ),
        migrations.DeleteModel(
            name='Resposta',
        ),
    ]
