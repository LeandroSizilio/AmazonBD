# Generated by Django 5.1.3 on 2024-11-27 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_servico_tipo_servico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='cliente',
        ),
        migrations.AddField(
            model_name='cliente',
            name='servico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.tiposervico'),
        ),
    ]