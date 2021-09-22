# Generated by Django 3.0.6 on 2020-06-04 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_notificacoes_setor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
                ('tipo_cont', models.TextField()),
                ('codigo', models.TextField()),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('tipo', models.TextField(blank=True, null=True)),
                ('data_pedido', models.DateTimeField()),
                ('status', models.TextField(blank=True, null=True)),
                ('produtos', models.ManyToManyField(to='app.Produto')),
            ],
        ),
    ]