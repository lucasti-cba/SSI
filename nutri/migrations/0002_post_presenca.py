# Generated by Django 3.0.6 on 2020-07-18 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('post', models.TextField()),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.IntegerField()),
                ('presenca', models.TextField()),
                ('data', models.DateField()),
            ],
        ),
    ]