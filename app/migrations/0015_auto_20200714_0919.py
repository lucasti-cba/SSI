# Generated by Django 3.0.6 on 2020-07-14 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20200610_1415'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estoque',
            options={'ordering': ['produto']},
        ),
    ]
