# Generated by Django 4.0.6 on 2022-08-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ativo',
            field=models.BooleanField(default=False),
        ),
    ]
