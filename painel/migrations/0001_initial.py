# Generated by Django 3.0.6 on 2020-06-16 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Senha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senha', models.TextField()),
                ('status', models.TextField()),
            ],
        ),
    ]