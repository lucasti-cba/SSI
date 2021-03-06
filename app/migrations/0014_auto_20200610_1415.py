# Generated by Django 3.0.6 on 2020-06-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200609_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='produtosCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('produtos', models.ManyToManyField(to='app.Produto')),
            ],
        ),
        migrations.AlterField(
            model_name='compra',
            name='produtos',
            field=models.ManyToManyField(to='app.produtosCompra'),
        ),
    ]
