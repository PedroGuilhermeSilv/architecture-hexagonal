# Generated by Django 5.1.1 on 2024-09-04 01:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlocacao',
            name='locacao',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='locacao.locacao'),
        ),
    ]
