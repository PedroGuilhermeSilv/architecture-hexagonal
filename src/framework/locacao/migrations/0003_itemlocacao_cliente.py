# Generated by Django 5.1.1 on 2024-09-05 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('locacao', '0002_alter_itemlocacao_locacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlocacao',
            name='cliente',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente'),
        ),
    ]
