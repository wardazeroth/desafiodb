# Generated by Django 5.0.6 on 2024-06-20 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_curso_alter_estudiante_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adltest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo1', models.CharField(max_length=100)),
                ('valor1', models.IntegerField(max_length=100)),
            ],
        ),
    ]