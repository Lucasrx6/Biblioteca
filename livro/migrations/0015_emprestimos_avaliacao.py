# Generated by Django 4.0.6 on 2022-08-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0014_alter_emprestimos_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='avaliacao',
            field=models.CharField(choices=[('P', 'Pessimo'), ('O', 'Otimo'), ('R', 'Ruim'), ('B', 'Bom')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
