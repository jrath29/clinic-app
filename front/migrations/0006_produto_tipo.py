# Generated by Django 5.0.3 on 2024-04-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_alter_produto_validade'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Farmaco', 'Farmaco'), ('Instrumento', 'Instrumento')], max_length=11, null=True),
        ),
    ]
