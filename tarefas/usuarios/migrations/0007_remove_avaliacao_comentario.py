# Generated by Django 4.2.17 on 2024-12-13 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_remove_avaliacao_cliente_avaliacao_avaliador_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='comentario',
        ),
    ]
