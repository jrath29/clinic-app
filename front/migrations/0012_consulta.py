# Generated by Django 5.0.3 on 2024-04-08 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0011_doutor_especialidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField()),
            ],
        ),
    ]
