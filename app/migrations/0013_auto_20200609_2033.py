# Generated by Django 3.0.6 on 2020-06-10 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200609_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagemProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagens', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='produto',
            name='imagens',
        ),
        migrations.AddField(
            model_name='produto',
            name='imagens',
            field=models.ManyToManyField(to='app.ImagemProduto'),
        ),
    ]