# Generated by Django 5.1.3 on 2024-11-27 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_tiposervico_custo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiposervico',
            name='custo',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
