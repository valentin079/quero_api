# Generated by Django 4.2.6 on 2023-10-25 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quero_delivery', '0003_alter_endereco_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='quantidade',
        ),
    ]
