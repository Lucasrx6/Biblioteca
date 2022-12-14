# Generated by Django 4.0.6 on 2022-08-31 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0017_alter_emprestimos_avaliacao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimos',
            name='tempo_duracao',
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='avaliacao',
            field=models.CharField(blank=True, choices=[('P', 'Pessimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Otimo')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 31, 16, 8, 6, 823043)),
        ),
    ]
