# Generated by Django 5.0.3 on 2024-04-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0009_alter_doutor_id_alter_paciente_id_alter_produto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doutor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]